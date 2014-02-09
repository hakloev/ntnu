package sokoban1;

import java.io.*;
import java.util.ArrayList;
import javax.swing.JOptionPane;

// class to create arraylist of level
public class SokobanLevelGet {
	
	// field for level list
	private ArrayList<String> list;
	
	// returns level
	public ArrayList<String> getLevel(int lvl) {
		if (lvl == 0) { // if 0 the user will create own level
			return ownLevel();
		}
		list = new ArrayList<String>();
		try {
			// reads in level txt file from inside project (so it can read inside jar file)
			list.clear();
			InputStream fil = getClass().getResourceAsStream("/sokoban_levels/00" + lvl + ".txt");
			InputStreamReader fr = new InputStreamReader(fil, "utf-8");
			BufferedReader br = new BufferedReader(fr);
			String line;
			while ((line = br.readLine()) != null) {
				list.add(line);
			}
			br.close();
			fr.close();
		}	
		catch (IOException e) {
			System.out.println(e);
		}
		return list;
	}

	// returns user-created level
	private ArrayList<String> ownLevel() {
		list = new ArrayList<String>();
		String input = null;
		Integer count = 1;
		try {
			int limit = Integer.parseInt(JOptionPane.showInputDialog(null, "Welcome to 'Create your" +
					" own level'\n\nHow many lines is your level?", "CREATE LEVEL", JOptionPane.INFORMATION_MESSAGE));
			while (count <= limit) {
				input = JOptionPane.showInputDialog(null, "Total lines in this level is" +
						" " + limit +  "\n\nEnter line " + count + ":", "CREATING LEVEL, LINE " + count, JOptionPane.INFORMATION_MESSAGE);
				list.add(input);
				count++;
			}
		}
		catch (NumberFormatException e) {
			
		}
		return list;
	}
}
	
