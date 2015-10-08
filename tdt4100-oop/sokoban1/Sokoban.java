
package sokoban1;

import java.awt.Color;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JOptionPane;

// class to create JFrame and make it possible to make jar file
public class Sokoban {
	
	// fields for applet and frame
	private static SokobanGraphics sokobanApplet;
	private static JFrame frame;
	private static final String version = "v1.5.6";
	
	// main method
	public static void main(String[] args) {
        // Create a frame for the applet to be displayed in
        frame = new JFrame();
        
        // Display the info-text
        showText(); 
        
        // Create menu, and display it
        createMenu();
        
        // Make instance of Sokoban
        sokobanApplet = new SokobanGraphics();
        
        // Make it so that when the frame closes, our program exits
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        // Set screen location for frame
        frame.setLocation(400, 100);
         
        // Set the size of the frame
        frame.setSize(480, 540);
         
        // Set frame background color
        frame.setBackground(Color.LIGHT_GRAY);
        
        // Let the applet recieve keyboard events from the frame
        frame.addKeyListener(sokobanApplet);
                
        // Add the applet to the frame
        frame.add(sokobanApplet);
   
        // Make the frame visible
        frame.setVisible(true);
   
        // Call the applet's init method
        sokobanApplet.init();
         
        // Call the applet's start method, this method will call GraphicsProgram's run method,
        // which you may or may not be overwriting in your project.
        // Either way you have to call the start method to start the applet.
        sokobanApplet.start();   
	 }
	
	// show text in frame
	private static void showText() {
		// Welcome text and controls info
        frame.getContentPane().setLayout(null);
        
        JLabel welcome = new JLabel("Welcome to hakloevs Sokoban " + version);
        welcome.setFont(new Font("Serif", Font.BOLD, 26));
        welcome.setBounds(35, 0, 500, 50);
        frame.getContentPane().add(welcome);
        
        JLabel info1 = new JLabel("or use the menubar");
        JLabel info2 = new JLabel("Press N for next level");
        JLabel info3 = new JLabel("Press P for previous level");
        JLabel info4 = new JLabel("Press R to restart level");
        JLabel info5 = new JLabel("Press ESC to quit game");
        JLabel start = new JLabel("Click inside app to start!");
         
        start.setFont(new Font("Serif", Font.BOLD, 20));
        
        info1.setBounds(165, 430, 400, 20);
        info2.setBounds(165, 350, 400, 20);
        info3.setBounds(165, 370, 400, 20);
        info4.setBounds(165, 390, 400, 20);
        info5.setBounds(165, 410, 400, 20);
        start.setBounds(130, 450, 400, 50);

        frame.getContentPane().add(info1);
        frame.getContentPane().add(info2);
        frame.getContentPane().add(info3);
        frame.getContentPane().add(info4);
        frame.getContentPane().add(info5);
        frame.getContentPane().add(start);
	}
	
	// creates menu in frame
	private static void createMenu() {
		 // Menu bar
        JMenuBar mb = new JMenuBar();
        JMenu file = new JMenu("File");
        mb.add(file);
        JMenu lvl = new JMenu("Levels");
        mb.add(lvl);
        JMenu help = new JMenu("Help");
        mb.add(help);
        JMenuItem exit = new JMenuItem("Exit");
        file.add(exit);
        JMenuItem usrLvl = new JMenuItem("Create your own");
        lvl.add(usrLvl);
        JMenuItem lvl1 = new JMenuItem("Level 1");
        lvl.add(lvl1);
        JMenuItem lvl2 = new JMenuItem("Level 2");
        lvl.add(lvl2);
        JMenuItem lvl3 = new JMenuItem("Level 3");
        lvl.add(lvl3);
        JMenuItem lvl4 = new JMenuItem("Level 4");
        lvl.add(lvl4);
        JMenuItem lvl5 = new JMenuItem("Level 5");
        lvl.add(lvl5);
        JMenuItem lvl6 = new JMenuItem("Level 6");
        lvl.add(lvl6);
        JMenuItem lvl7 = new JMenuItem("Level 7");
        lvl.add(lvl7);
        JMenuItem how = new JMenuItem("How to");
        help.add(how);
        JMenuItem about = new JMenuItem("About");
        help.add(about);
        
        
        // Set menu bar
        frame.setJMenuBar(mb);
         
        // Menu bar action listeners
        exit.addActionListener(new ActionListener() { // for exit button
        	@Override
			public void actionPerformed(ActionEvent e) {
				int terminate = JOptionPane.showConfirmDialog(null, "Are you sure you want to quit?", "TERMINATE", JOptionPane.YES_NO_OPTION);
				if (terminate == JOptionPane.YES_OPTION) { // if yes button
					System.exit(0); // system terminate
				}
			}
        }); 
        usrLvl.addActionListener(new ActionListener() { // for create own level
			@Override
			public void actionPerformed(ActionEvent e) {
				sokobanApplet.setLevel(0); // use applets setter, to set new level 
			}
		});
        lvl1.addActionListener(new ActionListener() { // for level 1
			@Override
			public void actionPerformed(ActionEvent arg0) {
				sokobanApplet.setLevel(1);
			}
		});
        lvl2.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent arg0) {
				sokobanApplet.setLevel(2);
			}
		});
        lvl3.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent arg0) {
				sokobanApplet.setLevel(3);
			}
		});
        lvl4.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent arg0) {
				sokobanApplet.setLevel(4);
			}
		});
        lvl5.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent arg0) {
				sokobanApplet.setLevel(5);
			}
		});
        lvl6.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent arg0) {
				sokobanApplet.setLevel(6);
			}
		});
        lvl7.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent arg0) {
				sokobanApplet.setLevel(7);
			}
		});
        how.addActionListener(new ActionListener() { // for "how to" button
			@Override
			public void actionPerformed(ActionEvent e) {
				JOptionPane.showMessageDialog(null, "Controls:\n" +
						"Control with arrow keys\nPress N for next level\n" +
						"Press P for previous level\nPress R to restart current level\n" +
						"Press ESC to quit\n\n" +
						"Create own level:\nTo create your own level, click 'Create your own'\n" +
						"Then enter how many lines you want, and\nenter one and one line\n" +
						"@ player, # wall, $ box\n. target, * box on target, + player on target,\nand one" +
						" space-character is empty space", "HOW" +
						" TO", JOptionPane.INFORMATION_MESSAGE);
			}
		});
        about.addActionListener(new ActionListener() { // for about-button
			@Override
			public void actionPerformed(ActionEvent arg0) {
				showAbout(); // calls about-method
			}
		});
	}
	
	private static void showAbout() { // displays about-message
		JOptionPane.showMessageDialog(null, "Sokoban " + version + "\n\nCreated by Håkon Ødegård Løvdal" +
				"\nFebruary 2013", "ABOUT", JOptionPane.INFORMATION_MESSAGE);
	}
}
