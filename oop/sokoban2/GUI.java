package sokoban2;

import java.awt.Color;
import java.awt.event.KeyEvent;
import java.io.IOException;
import java.util.EmptyStackException;

import javax.swing.JOptionPane;

import sokoban1.SokobanBoard;

import acm.graphics.GImage;
import acm.program.GraphicsProgram;

public class GUI extends GraphicsProgram implements GridListener {
	
	public Logic lvl;
	public GetLevel getLevel;
	private boolean canUndoMove = true;
	
	public void init() {
		getLevel = new GetLevel();
		addKeyListeners();
		setBackground(Color.LIGHT_GRAY);
		
	}
	
	public void run() {
		
	}
	
	public void displayLevel() throws NullPointerException {
		removeAll();
		int maxWidth = 0;
		for (int i = 0; i < lvl.getGridHeight(); i++) {
			if (lvl.getGridWidth(i) > maxWidth) {maxWidth = lvl.getGridWidth(i);}
			for (int j = 0; j < lvl.getGridWidth(i); j++) {
				char pos = lvl.getCell(j, i);
				GImage image = createImage(pos);
				image.setLocation(Constants.IMGSIZE * j, Constants.IMGSIZE * i);
				add(image);
			}
		}
		setSize(Constants.IMGSIZE * maxWidth, Constants.IMGSIZE* lvl.getGridHeight());
		int middleWidth = maxWidth / 2;
		int middleHeight = lvl.getGridHeight() / 2;
		setLocation(240 - (middleWidth * 16), 145 - (middleHeight * 16));
	}
	
	private GImage createImage(char pos) {
		switch (pos) {
		case SokobanBoard.WALL: 
			return new GImage(Constants.PATH_TO_IMAGE + "wall16x16.png"); 
		case SokobanBoard.EMPTY:
			return new GImage(Constants.PATH_TO_IMAGE  + "blank16x16.png"); 
		case SokobanBoard.TARGET:
			return new GImage(Constants.PATH_TO_IMAGE  + "target16x16.png"); 
		case SokobanBoard.PLAYER:
			return new GImage(Constants.PATH_TO_IMAGE  + "mover16x16.png"); 
		case SokobanBoard.PLAYER_TARGET:
			return new GImage(Constants.PATH_TO_IMAGE  + "mover_on_target16x16.png");  
		case SokobanBoard.BOX:
			return new GImage(Constants.PATH_TO_IMAGE  + "movable16x16.png"); 
		case SokobanBoard.BOX_TARGET:
			return new GImage(Constants.PATH_TO_IMAGE  + "movable_on_target16x16.png"); 
		default: 
			System.err.println("createImage: Invalid char, creating blank");
			return new GImage(Constants.PATH_TO_IMAGE  + "blank16x16.png"); 
		}
	}
	
	@Override
	public void gridChanged(Board b) {
//		System.out.println("works");
		displayLevel();
	}
		
	public void keyPressed(KeyEvent event) {
		int key = event.getKeyCode();
		switch (key) {
			case KeyEvent.VK_UP:
				if (canUndoMove) {
					if (lvl != null) {lvl.doMove(Direction.NORTH);}
				}
				break;
			case KeyEvent.VK_DOWN:
				if (canUndoMove) {
					if (lvl != null) {lvl.doMove(Direction.SOUTH);}
				}				
				break;
			case KeyEvent.VK_LEFT:
				if (canUndoMove) {
					if (lvl != null) {lvl.doMove(Direction.WEST);}
				}
				break;
			case KeyEvent.VK_RIGHT:
				if (canUndoMove) {
					if (lvl != null) {lvl.doMove(Direction.EAST);}
				}				
				break;
			case KeyEvent.VK_BACK_SPACE:
				if (canUndoMove) {
					if (lvl.canUndo()) {
						lvl.undoMove();
					} else {
						System.err.println("keyPressed: can't undo more moves");
					}
				}
				break;
			case KeyEvent.VK_U: 
				try {
					lvl.doUndoMove();
				} catch (EmptyStackException e) {
					System.err.println("keyPressed: empty stack, can't redo move");
				}
				break;
			case KeyEvent.VK_S:
				System.out.println("Her kommer save");
				break;
			case KeyEvent.VK_P:
				if (lvl != null) {
					String totMoves = lvl.getMoveList();
					for (int i = 0; i < totMoves.length(); i++) {
						if (i % 30 == 0) {
							totMoves = new StringBuffer(totMoves).insert(i, "\n").toString();
						}
					}
					JOptionPane.showMessageDialog(null, totMoves);
				}
				break;
			case KeyEvent.VK_ESCAPE:
				System.exit(0);
				break;
			case KeyEvent.VK_2: 
				String choice = JOptionPane.showInputDialog(null, "Choose level, 1-7", "CHOOSE LEVEL", JOptionPane.INFORMATION_MESSAGE);
				try {
					getLevel.getFromFile(Integer.parseInt(choice));
				} catch (NullPointerException e) {
				} catch (IOException e) {
				} catch (NumberFormatException e) {
				}
				lvl = new Logic(getLevel.getLines());
				canUndoMove = true;
				break;
			case KeyEvent.VK_1:
				String choice1 = JOptionPane.showInputDialog(null, "Choose level, enter url", "CHOOSE LEVEL", JOptionPane.INFORMATION_MESSAGE);
				try {
					if (choice1.equals("url")) {
						getLevel.getFromUrl(Constants.DEFAULT_LEVEL_URL);
					} else {
						getLevel.getFromUrl(choice1);
					}
				} catch (IOException e) {
					e.printStackTrace();
				}
				lvl = new Logic(getLevel.getLines());
				canUndoMove = true;
				break;
			case KeyEvent.VK_L:
				System.out.println("Her kommer load");
				break;
			default:
				System.err.println("keyPressed: Not valid key");
				break;
		}
		if (lvl.victory()) {System.out.println("Congratulations, level done"); canUndoMove = false;}
	}

	public void makeLevel(String[] lines) {
		lvl = new Logic(lines);
		lvl.addListner(this);
		displayLevel();
	}
	
	public void setCanUndoMove(boolean condition) {
		canUndoMove = condition;
	}

	
}