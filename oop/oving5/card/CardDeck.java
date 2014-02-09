package oving5.card;

import java.util.ArrayList;

public class CardDeck {
	
	// Instance-fields
	private ArrayList<Card> deck;
	
	/**
	 * Constructor, creates deck-ArrayList
	 */
	public CardDeck() {
		deck = new ArrayList<Card>();
		String[] suits = {"S", "H", "D", "C"}; // String array of valid suits
		for (int i = 0; i < suits.length; i++) {
			for (int j = 1; j < 14; j++) {
				Card card = new Card(suits[i], j); // Create card
				deck.add(card); // Add card to deck
			}
		}
	}
	
	/**
	 * @return deck.size();
	 */
	public int getCardCount() {
		return deck.size();
	}
	
	/**
	 * @param index
	 * @return Card card
	 */
	public Card getCard(int index) {
		if ((index >= 0) && (index < getCardCount())) {
			return deck.get(index); 
		}
		return null; // return null if card-index not in deck
	}
	
	/**
	 * @param numOfCards
	 * @return ArrayList<Card> cards
	 */
	public ArrayList<Card> deal(int numOfCards) {
		ArrayList<Card> cards = new ArrayList<Card>(); // temp ArrayList of cards
		if (this.deck.size() >= numOfCards) {
			for (int i = 0; i < numOfCards; i++) {
				int lastIndex = (deck.size() - 1); // temp variable for lastIndex in deck
				cards.add(deck.get((lastIndex)));
				deck.remove(lastIndex); // remove card from deck if added to cards
			}
			return cards; // return ArrayList
		} else {
			return null; // return null if numOfCards > size of deck
		}
	}
	
	
}
