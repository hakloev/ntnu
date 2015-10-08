package oving5.card;

public class Card {
	
	// Instance-fields
	private String suit; // holds value of suit
	private int face; // holds value of face
	
	/**
	 * public constructor, sets suit and face if valid parameter is given
	 * @param suit
	 * @param face
	 */
	public Card(String suit, int face) {
		// check face
		if ((face >= 0) && (face <= 13)) {
			this.face = face;
		} else {
			this.face = -1; // sets to -1 if invalid argument
		}
		
		// check suit
		if ("SHDC".contains(suit)) {
			this.suit = suit;
		} else {
			this.suit = null; // sets to null if invalid argument
		}
	}
	
	/**
	 * @return suit
	 */
	public String getSuit() {
		return this.suit;
	}
	
	/**
	 * @return face
	 */
	public int getFace() {
		return this.face;
	}
	
	/**
	 * toString()
	 * @Override
	 */
	@Override
	public String toString() {
		return (suit + face);
	}
	
}
