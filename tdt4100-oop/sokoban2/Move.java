package sokoban2;

public class Move {
	
	private Direction direction;
	private boolean isPush;
	private String typeOfMove;
	
	public Move(Direction direction, boolean push) {
		this.direction = direction;
		this.isPush = push;
		moveType();
	}
	
	private void moveType() {
		switch (this.direction) {
			case NORTH: typeOfMove = "u"; break;
			case SOUTH: typeOfMove = "d"; break;
			case WEST: typeOfMove = "l"; break;
			case EAST: typeOfMove = "r"; break;
			default: typeOfMove = "q"; break; // Shall/Will not happen
		
		}
		if (this.isPush) {
			typeOfMove = typeOfMove.toUpperCase();
		}
	}
	
	public Direction getDirection() {
		return this.direction;
	}
	
	public String toString() {
		return typeOfMove;
	}
}
