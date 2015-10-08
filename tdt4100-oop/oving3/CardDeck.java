package oving3;

import java.util.ArrayList;
import acm.graphics.GImage;
import acm.program.GraphicsProgram;

public class CardDeck extends GraphicsProgram{
	
	// Oppretter en arraylist cards, som skal ta vare på alle kort i stokken
	ArrayList<Card> cards;
	
	public void init() {
		// Initaliserer cards-arraylista
		cards = new ArrayList<Card>();
		// String-liste suits, som inneholder de fire typene kort
		String[] suits = {"S", "H", "D", "C"};
		/*
		 * Dobbel for-løkke 
		 * i går fra 0 til lengden av suits
		 * j går fra 1 til 13 (vanlig kortstokk
		 * Ytre-løkke henter type kort 
		 * Indre-løkke henter tall 
		 * Oppretter et objekt card med argumentene suit og j (type og tall)
		 * Legger til card i cards-arraylista
		 */
		for (int i = 0; i < suits.length; i++) {
			String suit = suits[i];
			for (int j = 1; j < 14; j++) {
				Card card = new Card(suit, j);
				cards.add(card);
			}
		} 
		// Initaliserer størrelsen på appleten
		setSize(650, 500);
	}
	
	public void run() {
		int x = 0, y = 0, counter = 0;
		for (Card c : cards) {
			GImage card = createGImage(c.suit, c.face);
			card.setLocation(x, y);
			add(card);
			x += 40;
			counter += 1;
			if (counter == 13) {
				counter = 0;
				x = 0;
				y += 90;
			}
		}
	}
	
	/**
	 * getCard-metode
	 * Returnerer card-objekt på angitt posisjon i cards-arraylista
	 * Tar ikke hensyn til exception 
	 * @param position
	 * @return card
	 */
	public Card getCard(int position) {
		if (position < cards.size()) {
			return cards.get(position);	
		}
		return null; 
	}	
	
	GImage createGImage(String suit, int value) {
		String name="";
		switch(suit.charAt(0)){
		case 'H':
			name+="hearts";
			break;
		case 'D':
			name+="diamonds";
			break;
		case 'C':
			name+="clubs";
			break;
		case 'S':
			name+="spades";
			break;
		}
		name+="-";
		switch(value) {
		case 1:
			name+="a";
			break;
		case 11:
			name+="j";
			break;
		case 12:
			name+="q";
			break;
		case 13:
			name+="k";
			break;
		default:
			name+="" + value;
		}

		name+="-150.png";
		return new GImage("oving3/img/" + name);
	}
}
