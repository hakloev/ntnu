package oving3;

import acm.program.ConsoleProgram;

public class Card extends ConsoleProgram {
	// Oppretter to felter til klassen
	String suit;
	int face;
	
	public Card() {
		
	}
	/**
	 * Tar inn to parameter og setter de til objektet vi arbeider på
	 * @param suit
	 * @param face
	 */
	public Card(String suit, int face) {
		this.suit = suit;
		this.face = face;
	}
	
	/**
	 * toString()-metode som returnerer suit+face for objektet
	 * @return string
	 */
	public String toString() {
		return (suit + face);
	}
}
