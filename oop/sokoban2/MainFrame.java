package sokoban2;

import java.awt.Color;
import java.awt.JobAttributes;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.IOException;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JOptionPane;

public class MainFrame extends JFrame {
	
	private GUI sokobanApplet;
	
	public MainFrame()  {
		sokobanApplet = new GUI();
		createGUI();
	}

	private void createGUI() {
		setTitle("hakloevs sokoban");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocation(400, 100);
        setSize(480, 540);
        setBackground(Color.LIGHT_GRAY);
		
        JButton url = new JButton("Get level from URL");
	    url.setSize(160, 40);
	    url.setLocation(60, 350);
	    getContentPane().add(url);
	        
	    JButton file = new JButton("Get level from file");
	    file.setSize(160, 40);
	    file.setLocation(260, 350);
	    getContentPane().add(file);
	    
	    JButton moves = new JButton("Print moves");
	    moves.setSize(160, 40);
	    moves.setLocation(60, 400);
	    getContentPane().add(moves);
	        
	    JButton undo = new JButton("Undo move");
	    undo.setSize(160, 40);
	    undo.setLocation(260, 400);
	    getContentPane().add(undo);

	    url.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				String choice = JOptionPane.showInputDialog(null, "Choose level, enter url", "CHOOSE LEVEL", JOptionPane.INFORMATION_MESSAGE);
				try {
					if (choice.equals("url")) {
						sokobanApplet.getLevel.getFromUrl(Constants.DEFAULT_LEVEL_URL);
					} else {
						sokobanApplet.getLevel.getFromUrl(choice);
					}
					sokobanApplet.makeLevel(sokobanApplet.getLevel.getLines());
					sokobanApplet.setCanUndoMove(true);
				} catch (IOException e1) {
				}
			}
		});
	    
	    file.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				String choice = JOptionPane.showInputDialog(null, "Choose level, 1-7", "CHOOSE LEVEL", JOptionPane.INFORMATION_MESSAGE);
				try {
					sokobanApplet.getLevel.getFromFile(Integer.parseInt(choice));
					sokobanApplet.makeLevel(sokobanApplet.getLevel.getLines());
					sokobanApplet.setCanUndoMove(true);
				} catch (NullPointerException e1) {
				} catch (IOException e1) {
				} catch (NumberFormatException e1) {
				}
			}
		}); 
	    
	    moves.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				if (sokobanApplet.lvl != null) {
					String totMoves = sokobanApplet.lvl.getMoveList();
					for (int i = 0; i < totMoves.length(); i++) {
						if (i % 30 == 0) {
							totMoves = new StringBuffer(totMoves).insert(i, "\n").toString();
						}
					}
					
					JOptionPane.showMessageDialog(null, totMoves);
				}
			}
		});
	    
	    undo.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				try {
					if (sokobanApplet.lvl.canUndo()) {
						sokobanApplet.lvl.undoMove();
						sokobanApplet.displayLevel();
					}
				} catch (NullPointerException ex) {
					
				}
			}
		});
	    
        add(sokobanApplet);
		addKeyListener(sokobanApplet);
		
		setVisible(true);
        
		sokobanApplet.init();
		sokobanApplet.start();
		
	}

}
