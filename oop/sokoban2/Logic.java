package sokoban2;

import java.util.ArrayList;
import java.util.EmptyStackException;
import java.util.List;
import java.util.Stack;

import sokoban1.SokobanBoard;

public class Logic extends Board {
	
	private Stack<Move> previousMoves; // stack of previous moves
	private Stack<Move> movesUndone;
	private boolean debug = false;
	private List<GridListener> listners;
	
	public Logic(String[] level) {
		super(level); // instance of board	
		previousMoves = new Stack<Move>();
		movesUndone = new Stack<Move>();
		listners = new ArrayList<GridListener>();
	}
	
	public void addListner(GridListener e) {
		listners.add(e);
	}
	
	private void fireBoardChanged() {
		for (GridListener e : listners) {
			((GridListener) e).gridChanged(this);
		}
	}
	
	public void doUndoMove() throws EmptyStackException {
		Move prevUndo = movesUndone.pop();
		Direction dir = prevUndo.getDirection();
		int nextX = super.getPlayerX() + dir.dx();
		int nextY = super.getPlayerY() + dir.dy();
		char nextPos = super.getCell(nextX, nextY);
		if (debug) {System.out.println("premove: " + getPlayerX() + getPlayerY());}
		if (debug) {System.out.println(nextPos);}
		if (checkMove(nextPos, dir)) {
			Move move = null;
			switch (nextPos) {
				case Constants.EMPTY: 
					moveToEmpty(nextX, nextY);
					move = new Move(dir, false);
					break;
				case Constants.TARGET: 
					moveToTarget(nextX, nextY);
					move = new Move(dir, false);
					break;
				case Constants.BOX: 
					moveBoxToNext(nextX, nextY, dir); 
					move = new Move(dir, true);
					break;
				case Constants.BOX_ON_TARGET: 
					moveBoxOnTargetToNext(nextX, nextY, dir); 
					move = new Move(dir, true);
					break;
			}
			super.setPlayerX(nextX);
			super.setPlayerY(nextY);
			fireBoardChanged();
			if (move != null) {previousMoves.push(move);}
			if (debug) {System.out.println("nachmove: " + getPlayerX() + getPlayerY());}
			if (debug) {System.out.println(super.toString());}
			}
	}
	
	public void doMove(Direction dir) {
		int nextX = super.getPlayerX() + dir.dx();
		int nextY = super.getPlayerY() + dir.dy();
		char nextPos = super.getCell(nextX, nextY);
		if (debug) {System.out.println("premove: " + getPlayerX() + getPlayerY());}
		if (debug) {System.out.println(nextPos);}
		if (checkMove(nextPos, dir)) {
			Move move = null;
			switch (nextPos) {
				case Constants.EMPTY: 
					moveToEmpty(nextX, nextY);
					move = new Move(dir, false);
					break;
				case Constants.TARGET: 
					moveToTarget(nextX, nextY);
					move = new Move(dir, false);
					break;
				case Constants.BOX: 
					moveBoxToNext(nextX, nextY, dir); 
					move = new Move(dir, true);
					break;
				case Constants.BOX_ON_TARGET: 
					moveBoxOnTargetToNext(nextX, nextY, dir); 
					move = new Move(dir, true);
					break;
			}
			super.setPlayerX(nextX);
			super.setPlayerY(nextY);
			movesUndone.clear();
			fireBoardChanged();
			if (move != null) {previousMoves.push(move);}
			if (debug) {System.out.println("nachmove: " + getPlayerX() + getPlayerY());}
			if (debug) {System.out.println(super.toString());}
		}
	}
	
	public void undoMove() {
		Move move = previousMoves.pop();
		String direction = move.toString();
		int newPlayerX = super.getPlayerX() + move.getDirection().opposite().dx();
		int newPlayerY = super.getPlayerY() + move.getDirection().opposite().dy();
		if ("udlr".contains(direction)) { // if not push
			undoPlayerPosistion(newPlayerX, newPlayerY);
			undoWithoutPush();
			movesUndone.push(move);
			fireBoardChanged();
		} else if ("UDLR".contains(direction)) { // if push
			undoPlayerPosistion(newPlayerX, newPlayerY);
			undoWithPush(move.getDirection());
			movesUndone.push(move);
			fireBoardChanged();
		} else {
			System.err.println("undoMove: invalid undo-direction"); // will/shall never happen
		}
		super.setPlayerX(newPlayerX); // update player position after undo move
		super.setPlayerY(newPlayerY);
	}
	
	private void undoWithPush(Direction dir) {
		if (debug) {System.out.print("undoWithPush: ");}
		int previousBoxX = super.getPlayerX() + dir.dx(); 
		int previousBoxY = super.getPlayerY() + dir.dy();
		if (super.isTarget(super.getPlayerX(), super.getPlayerY())) {
			super.setCell(super.getPlayerX(), super.getPlayerY(), Constants.BOX_ON_TARGET);
			if (debug) {System.out.print("newBoxPosTarget ");}
		} else {
			super.setCell(super.getPlayerX(), super.getPlayerY(), Constants.BOX);
			if (debug) {System.out.print("newBoxPosNotTarget ");}
		}
		if (super.isTarget(previousBoxX, previousBoxY)) {
			super.setCell(previousBoxX, previousBoxY, Constants.TARGET);
			if (debug) {System.out.print("prevBoxPosTarget\n");}
		} else {
			super.setCell(previousBoxX, previousBoxY, Constants.EMPTY);
			if (debug) {System.out.print("prevBoxPosNotTarget\n");}
		}
	}

	private void undoWithoutPush() {
		if (debug) {System.out.print("undoWithoutPush: ");}
		if (super.isTarget(super.getPlayerX(), super.getPlayerY())) {
			super.setCell(super.getPlayerX(), super.getPlayerY(), Constants.TARGET);	
			if (debug) {System.out.print(" prevPosTarget\n");}
		} else {
			super.setCell(super.getPlayerX(), super.getPlayerY(), Constants.EMPTY);
			if (debug) {System.out.print(" prevPosNotTarget\n");}
		}
	}
	
	private void undoPlayerPosistion(int newPlayerX, int newPlayerY) {
		if (debug) {System.out.print("undoPlayerPosition: ");}
		if (super.isTarget(newPlayerX, newPlayerY)) {
			super.setCell(newPlayerX, newPlayerY, Constants.PLAYER_ON_TARGET);
			if (debug) {System.out.print("newPlayerPosTarget\n");}
		} else {
			super.setCell(newPlayerX, newPlayerY, Constants.PLAYER);
			if (debug) {System.out.print("newPlayerPosNotTarget\n");}
		}
	}
	
	private void moveBoxOnTargetToNext(int nextX, int nextY, Direction dir) {
		int nextBoxPosX = (super.getPlayerX() + (dir.dx() * 2));
		int nextBoxPosY = (super.getPlayerY() + (dir.dy() * 2));
		if (super.isTarget(nextBoxPosX, nextBoxPosY)) {
			super.setCell(nextBoxPosX, nextBoxPosY, Constants.BOX_ON_TARGET);
		} else {
			super.setCell(nextBoxPosX, nextBoxPosY, Constants.BOX);
		}
		
		super.setCell(nextX, nextY, Constants.PLAYER_ON_TARGET);
		setPreviousPlayerPosition();
	}

	private void moveBoxToNext(int nextX, int nextY, Direction dir) {
		int nextBoxPosX = (super.getPlayerX() + (dir.dx() * 2));
		int nextBoxPosY = (super.getPlayerY() + (dir.dy() * 2));		
		if (super.isTarget(nextBoxPosX, nextBoxPosY)) {
			super.setCell(nextBoxPosX, nextBoxPosY, Constants.BOX_ON_TARGET);
		} else {
			super.setCell(nextBoxPosX, nextBoxPosY, Constants.BOX);
		}
		
		super.setCell(nextX, nextY, Constants.PLAYER);
		setPreviousPlayerPosition();
		
	}

	private void moveToTarget(int nextX, int nextY) {
		super.setCell(nextX, nextY, Constants.PLAYER_ON_TARGET);
		setPreviousPlayerPosition();
	}

	private void moveToEmpty(int nextX, int nextY) {
		super.setCell(nextX, nextY, Constants.PLAYER);
		setPreviousPlayerPosition();
	}
	
	private void setPreviousPlayerPosition() {
		if (super.isTarget(super.getPlayerX(), super.getPlayerY())) {
			super.setCell(super.getPlayerX(), super.getPlayerY(), Constants.TARGET);
		} else {
			super.setCell(super.getPlayerX(), super.getPlayerY(), Constants.EMPTY);
		}
	}

	private boolean checkMove(char nextPos, Direction dir) {
		switch (nextPos) {
			case Constants.WALL: return false;
			case Constants.EMPTY: return true;
			case Constants.TARGET: return true;
			case Constants.BOX: return canBoxMove(dir);
			case Constants.BOX_ON_TARGET: return canBoxMove(dir);
			default: System.err.println("checkMove: invalid level-character"); System.out.println(nextPos); return false;
		}
	}

	private boolean canBoxMove(Direction dir) {
		int nextBoxPosX = (super.getPlayerX() + (dir.dx() * 2));
		int nextBoxPosY = (super.getPlayerY() + (dir.dy() * 2));
		if (super.getCell(nextBoxPosX, nextBoxPosY) == Constants.EMPTY) {return true;}
		else if (super.getCell(nextBoxPosX, nextBoxPosY) == Constants.TARGET) {return true;}
		else if (super.getCell(nextBoxPosX, nextBoxPosY) == Constants.BOX_ON_TARGET) {return false;}
		else if (super.isTarget(nextBoxPosX, nextBoxPosY)) {return true;}
		else {return false;}
	}

	public boolean canUndo() {return previousMoves.size() > 0;}
	
	public String getMoveList() {
		String moves = "moves: ";
		if (debug) {System.out.println(previousMoves);}
		if (previousMoves != null) {
			for (Move m : previousMoves) {
				moves += m.toString();
			}
		}
		return moves;
	}
	
	public boolean victory() { // returns boolean, is player done with level
		int boxesOnTarget = 0;
		for (ArrayList<Character> row : super.getGrid()) {
			for (int i = 0; i < row.size(); i++) {
				if (row.get(i) == SokobanBoard.BOX_TARGET) {
					boxesOnTarget++;
				}
			} 
		} 
		if (boxesOnTarget == super.getNumOfTargets()) {
			return true;
		} 
		return false;
	} 

	public int getGridHeight() {return super.getGridHeight();}

	public int getGridWidth(int x) {return super.getGridWidth(x);}
	
	public char getCell(int x, int y) {return super.getCell(x, y);}
	
}
