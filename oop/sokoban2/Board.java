package sokoban2;

import java.util.ArrayList;
import java.util.List;

public class Board {

	private ArrayList<ArrayList<Boolean>> targets; // Holds the boolean location of targets
	private ArrayList<ArrayList<Character>> grid; // Hold the character location of board
	private int numOfTargets;
	private int playerX; // x is width
	private int playerY; // y is height
	
	public Board(String[] level) {
		targets = new ArrayList<ArrayList<Boolean>>();
		grid = new ArrayList<ArrayList<Character>>();
		try {
			createLevel(level);
		} catch (NullPointerException e) {
			System.err.println("createLevel: null-pointer exception");
		} catch (IllegalArgumentException e) {
			System.err.println("createLevel: not a valid level");
		}
	}

	private void createLevel(String[] level) throws NullPointerException {
		for (int i = 0; i < level.length; i++) {
			ArrayList<Boolean> rowTargets = new ArrayList<Boolean>();
			ArrayList<Character> rowGrid = new ArrayList<Character>();
			for (int j = 0; j < level[i].length(); j++) {
				char pos = level[i].charAt(j);
				switch (pos) {
					case Constants.WALL: 
						rowTargets.add(false);
						rowGrid.add(Constants.WALL);
						break;
					case Constants.EMPTY: 
						rowTargets.add(false);
						rowGrid.add(Constants.EMPTY);
						break;
					case Constants.TARGET: 
						rowTargets.add(true);
						rowGrid.add(Constants.TARGET);
						numOfTargets++;
						break;
					case Constants.PLAYER: 
						rowTargets.add(false);
						rowGrid.add(Constants.PLAYER);
						this.playerX = j;
						this.playerY = i;
						break;
					case Constants.PLAYER_ON_TARGET: 
						rowTargets.add(true);
						rowGrid.add(Constants.PLAYER_ON_TARGET);
						this.playerX = j;
						this.playerY = i;
						numOfTargets++;
						break;
					case Constants.BOX: 
						rowTargets.add(false);
						rowGrid.add(Constants.BOX);
						break;
					case Constants.BOX_ON_TARGET: 
						rowTargets.add(true);
						rowGrid.add(Constants.BOX_ON_TARGET);
						numOfTargets++;
						break;
					default: 
						System.err.println("createLevel: not valid level-character");
						break;
				}
			}
			targets.add(rowTargets);
			grid.add(rowGrid);
		}
		if (!(validLevel())) {
			throw new IllegalArgumentException("This level is not valid");
		} else {
			System.out.println("good level");
		}
	}
	
	private boolean validLevel() {
		int players=0, targetsInLevel=0, box=0, freeBox=0;
		for (ArrayList<Boolean> row : targets ) {
			for (Boolean e : row) {
				if (e) {
					targetsInLevel++;
				}
			}
		}
		for (ArrayList<Character> row : grid) {
			for (Character c : row) {
				if (c == '@' || c == '+') {
					players++;
				} else if (c == '$' || c == '*') {
					box++;
					if (c == '$') {
						freeBox++;
					}
				}
			}
		}
		if ((players == 1) && (targetsInLevel == box) && (freeBox >= 1)) {
			return true;
		}
		return false;
		
	}
	
	public char getCell(int x, int y) {
		try {
			return grid.get(y).get(x);
		} catch (IndexOutOfBoundsException e) {
			System.err.println("getCell: index out of bounds");
			return '#'; // wall as default-return 
		}
	}
	
	public void setCell(int x, int y, char type) {grid.get(y).set(x, type);}
	
	public boolean isTarget(int x, int y) {return targets.get(y).get(x);}
	
	public ArrayList<ArrayList<Character>> getGrid() {return grid;}

	public int getGridHeight() {return grid.size();}

	public int getGridWidth(int x) {return grid.get(x).size();}
	
	public int getNumOfTargets() {return numOfTargets;}
	
	public void setPlayerX(int x) {playerX = x;}
	
	public int getPlayerX() {return playerX;} 
	
	public void setPlayerY(int y) {playerY = y;}
	
	public int getPlayerY() {return playerY;} 

	public String toString() {
		String map = "";
		for (ArrayList<Character> c : grid) {
			map += c + "\n";
		}
		return map;
	}
}