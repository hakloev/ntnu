package oving6;

public class Card implements Comparable<Card> {
	
	private String suit;
	private int face;
	
	public Card(String suit, int face) {
		if ("SHDC".contains(suit)) {
			this.suit = suit;
		}
		if ((face >= 0) && (face <= 13)) {
			this.face = face;
		}
	}
	
	public String getSuit() {
		return this.suit;
	}
	
	public int getFace() {
		return this.face;
	}
	
	public String toString() {
		return (this.suit + this.face);
	}
	
	private int faceVal() {
		if (face == 1) {
			return 14;
		} else { 
			return face;
		}
	}

	@Override
	public int compareTo(Card o) {
		if (faceVal() != o.faceVal()) {
			return (faceVal() - o.faceVal());
		} else {
			return this.suit.compareTo(o.suit);
		}
	}
}

