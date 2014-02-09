package sokoban1;

import acm.graphics.GImage;
import acm.graphics.GLabel;
import acm.program.GraphicsProgram;
import java.awt.Color;
import java.awt.event.KeyEvent;
import javax.swing.JOptionPane;

// Class do display graphics and handle user-input
@SuppressWarnings("serial")
public class SokobanGraphics extends GraphicsProgram {
	
	// Fields-variables 
	private final static String PATH = "sokoban/";
	private final static int IMGSIZE = 16;
	private int currLvl = 1; // Always level 1 as default
	private SokobanMove level; // Create instance of move-class 
	
	// Initiate keyListeners etc
	public void init() {
		addKeyListeners();
		setSize(240, 300);
		setBackground(Color.BLACK);
		setLocation(120, 50); // set location in JFrame
	} // init
	
	public void run() {
		runLevel(); // Display first level
	} // run
	
	// Initializes level and displays it
	private void runLevel() {
		level = new SokobanMove(currLvl);
		displayLevel();
	} // runLevel
	
	// Paints level to screen
	public void displayLevel() {
		removeAll(); // removes all object every time method is called
		try { // Sorrounds with try, because empty level will cause nullpointerexception
			for (int i = 0; i < level.getSizeHeight(); i++) { // Get level line 
				for (int j = 0; j < level.getSizeWidth(i); j++) { // Get position in level line
					char position = level.getCell(i, j); // // Char of current position
					GImage image = createImage(position); // Call create image with position
					image.setLocation((IMGSIZE*j), (IMGSIZE*i)); // set location of image
					add(image); // add image
				} // inner for-loop
			} //outer for-loop
		} // try
		catch (NullPointerException e) {
			System.exit(0);
		} // catch
		// Displays label with nr of moves every time level is painted
		GLabel moves = new GLabel("Number of moves: " + level.getNumOfMoves());
		moves.setColor(Color.WHITE);
		moves.setLocation(45, 250);
		add(moves);
	} // displayLevel
	
	public GImage createImage(char position) {
		// position is char of position in level grid
		switch (position) {
			case SokobanBoard.WALL: 
				return new GImage(PATH + "wall16x16.png"); 
			case SokobanBoard.EMPTY:
				return new GImage(PATH + "blank16x16.png"); 
			case SokobanBoard.TARGET:
				return new GImage(PATH + "target16x16.png"); 
			case SokobanBoard.PLAYER:
				return new GImage(PATH + "mover16x16.png"); 
			case SokobanBoard.PLAYER_TARGET:
				return new GImage(PATH + "mover_on_target16x16.png"); 
			case SokobanBoard.PLAYER_BOX_TARGET:
				return new GImage(PATH + "mover_box_on_target16x16.png"); 
			case SokobanBoard.BOX:
				return new GImage(PATH + "movable16x16.png"); 
			case SokobanBoard.BOX_TARGET:
				return new GImage(PATH + "movable_on_target16x16.png"); 
			default: 
				System.out.println("createImage: Invalid char, creating blank");
				return new GImage(PATH + "blank16x16.png"); 
		} // switch	
	} // createImage
	
	public void keyPressed(KeyEvent event) {
		int key = event.getKeyCode(); 
		switch (key) {
			case KeyEvent.VK_UP:
				level.doMove(-1, 0); // (x, y) where x is height, y is width
				displayLevel();
				break;
			case KeyEvent.VK_DOWN:
				level.doMove(1, 0);
				displayLevel();
				break;
			case KeyEvent.VK_LEFT:
				level.doMove(0, -1);
				displayLevel();
				break;
			case KeyEvent.VK_RIGHT:
				level.doMove(0, 1);
				displayLevel();
				break;
			case KeyEvent.VK_ESCAPE:
				int terminate = JOptionPane.showConfirmDialog(null, "Are you sure you want to quit?", "TERMINATE", JOptionPane.YES_NO_OPTION);
				if (terminate == JOptionPane.YES_OPTION) {
					System.exit(0);					
				}
				break;
			case KeyEvent.VK_R:
				runLevel();
				break;
			case KeyEvent.VK_N:
				if ((currLvl + 1) > 7) {
					currLvl = 7;
				} else {
					currLvl++;
				}
				runLevel();
				break;
			case KeyEvent.VK_P:
				if ((currLvl - 1) < 0) {
					currLvl = 0;
				} else {
					currLvl--;					
				}
				runLevel();
				break;
		} // switch
		if (level.victory()) {
			GLabel victory1 = new GLabel("Congratulations");
			GLabel victory2 = new GLabel("You completed level " + currLvl);
			victory1.setLocation(65, 200);
			victory2.setLocation(45, 220);
			victory1.setColor(Color.WHITE);
			victory2.setColor(Color.WHITE);
			add(victory1);
			add(victory2);
		} // end-if
	} // keyPressed
	
	// setLevel, so the menu in Sokoban.java will work, and paint new level 
	public void setLevel(int lvl) {
		this.currLvl = lvl;
		runLevel();
	} // setLevel
	
} // SokobanGraphics

