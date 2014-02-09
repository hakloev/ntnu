package sokoban1;

import java.util.ArrayList;

import javax.swing.JOptionPane;

// class to handle movement on board (instance of SokobanBoard)
public class SokobanMove {
	
	// fields
	private SokobanBoard board; // board-field
	private int playerX; // player position, x is height
	private int playerY; // player position, y is width
	private int numOfTargets; // total of number targets
	private int numOfMoves; // total number of moves
	
	// constructor, creates instance of board and initialize field-variables
	public SokobanMove(int lvlNr) { // constructor for this class
		board = new SokobanBoard(lvlNr); // makes an instance of board
		this.playerX = board.getPlayerX(); // Initialize playerX and playerY
		this.playerY = board.getPlayerY(); // ** 
		this.numOfTargets = board.getNumTargets(); // Initialize numOfTargets
		this.numOfMoves = 0;  // initialize numOfMoves
	}
	
	// the method to determine move and excecute move-methods
	public void doMove(int x, int y) { // x is height, y is width
		int nextX = playerX + x; // temp-variables with next position
		int nextY = playerY + y; // **
		char nextPos = board.getCell(nextX, nextY); // get the type of next position
//		System.out.println(checkMove(nextPos, x, nextX, y, nextY)); // used for debug
		if (checkMove(nextPos, x, nextX, y, nextY)) { // check next position, if it's a valid move
			this.numOfMoves++;
			switch (nextPos) { // if move is valid, do move that depends of the type of nextPos
				case SokobanBoard.EMPTY: moveEmpty(nextX, nextY); break;
				case SokobanBoard.TARGET: moveTarget(nextX, nextY); break;
				case SokobanBoard.BOX: moveBox(nextX, nextY, x, y); break;
				case SokobanBoard.BOX_TARGET: moveBox(nextX, nextY, x, y); break;
			} // switch-end
			playerX = nextX; // changing player-coordinates after move,
			playerY = nextY; // that way I can use the fields in move-methods
			System.out.println(board); // used for debug
		} // if-end
	} // doMove
	
	private void moveTarget(int nextX, int nextY) {
		// no need for boolean isTarget for nextPos, already done in checkMove
		board.setCell(nextX, nextY, SokobanBoard.PLAYER_TARGET); // set next position to player on target
		if (board.isTarget(playerX, playerY)) { 
			board.setCell(playerX, playerY, SokobanBoard.TARGET); // set previous position to target
		} else { 
			board.setCell(playerX, playerY, SokobanBoard.EMPTY); // set previous position to empty
		} // end if
	} // moveTarget
	
	/*
	 * In moveBox and moveTarget I set the next grid to player box on target, when box is on target
	 * This is because I only want to see the "smile-mover" (mover_box_on_target) when I have
	 * pushed a box onto a target. I can do this because I read in boolean values of where the
	 * targets are when I create the level, and I never change that list. I also use that list
	 * to set the targets after me to targets again 
	 */
	private void moveBox(int nextX, int nextY, int x, int y) {
		int nextBoxX = nextX + x;
		int nextBoxY = nextY + y;
		if (!board.isTarget(playerX, playerY)) { // if player position !target 
//			System.out.println("1"); // used for debug
			if (board.isTarget(nextBoxX, nextBoxY)) { // if next box position target
//				System.out.println("2");
				board.setCell(nextBoxX, nextBoxY, SokobanBoard.BOX_TARGET); // nextBox position to box on target
				board.setCell(nextX, nextY, SokobanBoard.PLAYER_BOX_TARGET); // next position to player on target so we get smiley mover
				board.setCell(playerX, playerY, SokobanBoard.EMPTY); // current position to empty
			} else { // if next box position !target
//				System.out.println("3");
				board.setCell(nextBoxX, nextBoxY, SokobanBoard.BOX); // nextBox position to box
				board.setCell(nextX, nextY, SokobanBoard.PLAYER); // next position to player on target
				board.setCell(playerX, playerY, SokobanBoard.EMPTY); // current pos empty	
			} 
		} else { // if player position target
//			System.out.println("4");
			if (board.isTarget(nextBoxX, nextBoxY)) { // if next box position target
//				System.out.println("5");
				board.setCell(nextBoxX, nextBoxY, SokobanBoard.BOX_TARGET); // nextBox postiton to box on target
				board.setCell(nextX, nextY, SokobanBoard.PLAYER_BOX_TARGET); // next player pos to player_box_on_target
				board.setCell(playerX, playerY, SokobanBoard.TARGET); // prev player pos to target
			} else { // next box position !target 
//				System.out.println("6");
				board.setCell(nextBoxX, nextBoxY, SokobanBoard.BOX); // next box pos to box
				board.setCell(nextX, nextY, SokobanBoard.PLAYER); // next player pos to player
				board.setCell(playerX, playerY, SokobanBoard.TARGET); // prev player pos to target
			} 
		} // end if
	} // moveBox
	
	// Move if next space empty
	private void moveEmpty(int nextX, int nextY) {
		if (board.isTarget(playerX, playerY)) { // check if current position is target
			board.setCell(playerX, playerY, SokobanBoard.TARGET); // set current to target
			board.setCell(nextX, nextY, SokobanBoard.PLAYER);  // set next to player
		} else { // current position to empty
			board.setCell(nextX, nextY, SokobanBoard.PLAYER); // next to player
			board.setCell(playerX, playerY, SokobanBoard.EMPTY); // current to empty
		} // end if
	} // moveEmpty
	
	// returns bool about box move
	private boolean checkBoxMove(int x, int nextX, int y, int nextY) {
		int nextBoxX = nextX + x; // variable for next position of the box x
		int nextBoxY = nextY + y; // same, for y
//		System.out.println(nextBoxX);
//		System.out.println(nextBoxY);
		if (board.getCell(nextBoxX, nextBoxY) == SokobanBoard.EMPTY) { 
//			System.out.println("1"); // used for debug
			return true; // can move, nextBox position is empty
		} else if (board.getCell(nextBoxX, nextBoxY) == SokobanBoard.TARGET) {
//			System.out.println("2");
			return true; // can move, nextBox position is box on target
		} else if (board.getCell(nextBoxX, nextBoxY) == SokobanBoard.BOX_TARGET) {
//			System.out.println("3");
			return false; // cant move nextBox position is box on target
		} else if (board.isTarget(nextBoxX, nextBoxY)) {
//			System.out.println("4");
			return true; // can move, next position is target
		} else {
//			System.out.println("5");
			return false; // can't move, nextBox position is wall etc
		}
	} // checkBoxMove
	
	// check if the move is valid, calls helper-methods
	private boolean checkMove(char nextPos, int x, int nextX, int y, int nextY) {
		switch (nextPos) { // checks move, depends on char of nextPos
			case SokobanBoard.WALL: return false;
			case SokobanBoard.EMPTY: return true;
			case SokobanBoard.TARGET: return true;
			case SokobanBoard.BOX: return checkBoxMove(x, nextX, y, nextY); // it's box, must check if nextPos for box is valid
			case SokobanBoard.BOX_TARGET: return checkBoxMove(x, nextX, y, nextY);
			default: // default return if not valid char
				JOptionPane.showMessageDialog(null, "checkMove: Something went wrong, debug needed!", "DEBUG", JOptionPane.ERROR_MESSAGE); 
				return false;
		} // switch-end
	} // checkMove
	
	public int getSizeHeight() { // for easier to read code in SokobanGraphics, returns boards getSizeHeight
		return board.getSizeHeight();
	} // getSizeHeight
	
	public int getSizeWidth(int i) { // same as getSizeHeight, takes in current row
		return board.getSizeWidth(i);
	} // getSizeWidth
	
	public char getCell(int i, int j) { // same as getSizeHeight
		return board.getCell(i, j);
 	} // getCell
	
	public int getNumOfMoves() {
		// returns total num of moves 
		return this.numOfMoves;
	} // getNumOfMoves
	
	public boolean victory() { // returns boolean, is player done with level
		int boxesOnTarget = 0;
		for (ArrayList<Character> row : board.getGrid()) {
			for (int i = 0; i < row.size(); i++) {
				if (row.get(i) == SokobanBoard.BOX_TARGET) {
					boxesOnTarget++;
				}
			} // inner for-loop
		} // outer for-loop 
		if (boxesOnTarget == numOfTargets) {
			return true;
		} // end-if
		return false;
	} // victory
} //LevelMove
