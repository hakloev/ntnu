package oving1;

import java.awt.Dimension;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

import javax.swing.ButtonGroup;
import javax.swing.JCheckBox;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.JToggleButton;

public class ButtonsNText extends JPanel {

	private JTextField TextLine;
	private JToggleButton UpperCaseButton;
	private JToggleButton LowerCaseButton;
	private JCheckBox ContinuousButton;
	
	/**
	 * Constructor for ButtonsNText
	 * Initates buttons and textfield
	 */
	public ButtonsNText() {
		// Init components
		TextLine = new JTextField();
		TextLine.setPreferredSize(new Dimension(200, 20));	
		UpperCaseButton = new JToggleButton("Upper case");
		LowerCaseButton = new JToggleButton("Lower case");
		ContinuousButton = new JCheckBox("Continuous?");
		
		// setName for JUnit-tests
		TextLine.setName("TextLine");
		UpperCaseButton.setName("UpperCaseButton");
		LowerCaseButton.setName("LowerCaseButton");
		ContinuousButton.setName("ContinuousButton");
		
		// Init button group
		ButtonGroup btnGroup = new ButtonGroup();
		btnGroup.add(UpperCaseButton);
		btnGroup.add(LowerCaseButton);
		
		// Add all listeners
		KeyLstnr enterLstnr = new KeyLstnr();
		TextLine.addKeyListener(enterLstnr);
		
		BtnLstnr btnLstnr = new BtnLstnr();
		UpperCaseButton.addActionListener(btnLstnr);
		LowerCaseButton.addActionListener(btnLstnr);
		
		// Add all components 
		add(TextLine);
		add(UpperCaseButton);
		add(LowerCaseButton);
		add(ContinuousButton);
	}
	
	// Listener for Enter-key
	private class KeyLstnr implements KeyListener {
		
		@Override
		public void keyTyped(KeyEvent e) {

		}
		
		@Override
		public void keyPressed(KeyEvent e) {
			
		}

		@Override
		public void keyReleased(KeyEvent e) {
			if (e.getKeyCode() == KeyEvent.VK_ENTER) {
				replaceText();
            }
		    if (ContinuousButton.isSelected()) {
				replaceText();
			} 
		}	
	}
	
	// Listener for upper/lower-case keys
	private class BtnLstnr implements ActionListener {

		@Override
		public void actionPerformed(ActionEvent e) {
			replaceText();
		}
	}
	
	// Method to replace text with correct case
	private void replaceText() {
		int caretPos = TextLine.getCaretPosition();
		if (UpperCaseButton.isSelected()) {
			TextLine.setText(TextLine.getText().toUpperCase());
		} else if (LowerCaseButton.isSelected()) {
			TextLine.setText(TextLine.getText().toLowerCase());
		} else {
			
		}
		TextLine.setCaretPosition(caretPos);
	}
		
	/**
	 * Main method, to initate JFrame and add JPanel
	 * @param args
	 */
	public static void main(String[] args) {
		JFrame frame = new JFrame("Øving T1");
		frame.setContentPane(new ButtonsNText());
		frame.pack();
		frame.setVisible(true);
	}
	
	/**
	 * 
	 
	- In GUI programming, we distinguish between lexical, syntactical and semantical events. 
	  What kind of mechanisms did you use to handle lexical and syntactical events in your implementation?
	  	  
	  Syntaktiske hendelser skjer ved en kombinasjon av betingelser og hendelser. 
	  Abstraherer bort input-enhet. Dette er feks actionListeners og keyListeners i denne øvinga. 
	  ButtonGroup for å holde kontroll på at maks en av knappene
 	  er nede samtidig er også en syntaktisk hendelse

	  En syntaktisk hendelse tilsvarer en sekvens av leksikale hendelser. Koden blir
	  derfor kortere og lettere. 
	  
	  Leksikale hendelser forekommer i vinduet de intreffer i, feks keyEventene i denne øvinga. 
	  Dette er de minste enhetene brukerinteraksjon. getKeyCode() == KeyEvent.VK_ENTER er en leksikalsk hendelse.

	
	- What is the advantage of syntactical events compared to lexical events?
	
	  Fordelen med syntaktiske hendelser er at den gjerne har mindre komplisert logikk, 
	  og kan brukes på flere hendelser, ikke bare spesifikke enkelthendelser. 
	  Som sagt tidligere abstraherer den også bort input-enhet. 
	
	- Concerning the lexical events you answered for the first question above, could
	  you have handled syntactical event instead of lexical events?
	  
	 Kan ikke se noen annen måte å sjekke tastatur-inputen på en med keyEvents.  
	  
	 * 
	 */

}
