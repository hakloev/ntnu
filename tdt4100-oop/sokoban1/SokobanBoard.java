package sokoban1;

import java.util.ArrayList;

import javax.swing.JOptionPane;

// class to handle board (level)
public class SokobanBoard extends SokobanLevelGet {
	
	// public constants for the chars that represent gui
	public final static char WALL = '#';
	public final static char EMPTY = ' ';
	public final static char TARGET = '.';
	public final static char PLAYER = '@';
	public final static char PLAYER_TARGET = '+';
	public final static char PLAYER_BOX_TARGET = '-'; // I added this for smile when box on target
	public final static char BOX = '$';
	public final static char BOX_TARGET = '*';

	private ArrayList<ArrayList<Boolean>> targets; // Location of targets
	private ArrayList<ArrayList<Character>> grid; // Map 
	private int playerX, playerY, numTargets; 

	// Constructor, initializes level and level-getter 
	public SokobanBoard(int lvlNr) {
		targets = new ArrayList<ArrayList<Boolean>>(); // initializes targets array
		grid = new ArrayList<ArrayList<Character>>(); // initializes grid array
		createLevel(getLevel(lvlNr)); // getter returns array list of level
	} // LevelLogic()
	
	// creates level from arraylist
	private void createLevel(ArrayList<String> lvl) {
		for (int i = 0; i < lvl.size(); i++) {
			ArrayList<Boolean> rowTargets = new ArrayList<Boolean>(); // create temp row for targets array
			ArrayList<Character> rowGrid = new ArrayList<Character>(); // create temp row for grid array
			for (int j = 0; j < lvl.get(i).length(); j++) {
				char pos = lvl.get(i).charAt(j); // char of current position
				switch(pos) {
					case WALL: 
						rowTargets.add(false); // sets boolean to targets-array
						rowGrid.add(WALL); // sets char to grid-array
						break;
					case EMPTY: 
						rowTargets.add(false);
						rowGrid.add(EMPTY);
						break;
					case TARGET: 
						rowTargets.add(true);
						rowGrid.add(TARGET);
						this.numTargets++; // adds 1 to total number of targets
						break;
					case PLAYER: 
						rowTargets.add(false);
						rowGrid.add(PLAYER);
						this.playerX = i; // sets player position
						this.playerY = j; // sets player position
						break;
					case PLAYER_TARGET: 
						rowTargets.add(true);
						rowGrid.add(PLAYER_TARGET);
						this.playerX = i; 
						this.playerY = j;
						this.numTargets++;
						break;
					case PLAYER_BOX_TARGET:
						rowTargets.add(false);
						rowGrid.add(PLAYER_BOX_TARGET);
						this.playerX = i;
						this.playerY = j;
						break;
					case BOX:
						rowTargets.add(false);
						rowGrid.add(BOX);
						break;
					case BOX_TARGET: 
						rowTargets.add(true);
						rowGrid.add(BOX_TARGET);
						this.numTargets++;
						break;
					default:
						// displays error message if invalid char in level
						JOptionPane.showMessageDialog(null, "createLevel, invalid level-character", "DEBUG", JOptionPane.ERROR_MESSAGE);
						break;
				} // switch end
			} // inner for-loop
			targets.add(rowTargets); // add row to targets array
			grid.add(rowGrid); // add row to grid array
		} // outer for-loop
	} // createLevel
	
	public void setCell(int height, int width, char c) {
		// sets cell to char
		this.grid.get(height).set(width, c);
	} // setCell
	
	public char getCell(int height, int width) {
		// try to return the requested cell
		try {
			return this.grid.get(height).get(width);			
		}
		catch (IndexOutOfBoundsException e) {
			return '#'; // returns wall as default if array out of bounds
		}
	} // getCell
	
	public boolean isTarget(int height, int width) {
		// returns bool value of requested cell
		return this.targets.get(height).get(width);
	} // isTarget
	
	public int getSizeHeight() {
		// returns number of rows
		return this.grid.size();
	} // getSizeHeight
	
	public int getSizeWidth(int i) { // takes in current row
		// returns length of row
		return this.grid.get(i).size();
	} // getSizeWidth
	
	public ArrayList<ArrayList<Character>> getGrid() {
		// returns the grid-array
		return this.grid;
	} // getGrid
	
	public int getPlayerX() {
		// returns player pos
		return this.playerX;
	} // getPlayerX
	
	public int getPlayerY() {
		// returns player pos
		return this.playerY;
	} // getPlayerY
	
	public int getNumTargets() {
		// returns nr of targets
		return this.numTargets;
	} // getNumTargets

	@Override
	public String toString() {
		// override toString, returns string representation of level (grid)
		String map = "";
		for (ArrayList<Character> c : grid) {
			map += c + "\n";
		}
		return map;
	} // toString
	
} // LevelLogic