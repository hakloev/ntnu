package oving9;

import java.util.Arrays;
import java.util.Iterator;
import java.util.List;

import acm.graphics.GLabel;
import acm.program.GraphicsProgram;

public class HighscoreView extends GraphicsProgram implements ListListener {
	
	private List<String> persons = Arrays.asList("HŒkon", "Steinar", "Fredrik", "Kari", "Nils");
	private List<Integer> scores = Arrays.asList(10, 4, 8, 3, 1);
	
	private HighscoreList highscoreList;
	
	public HighscoreView() {
		highscoreList = new HighscoreList(10);
		highscoreList.addListListener(this);
	}
	
	public void init() {
		for (int i = 0; i < 10; i++) {
			String person = persons.get(Math.abs((int)(Math.random() * 10 - 5)));
			int score = scores.get(Math.abs((int)(Math.random() * 10 - 5)));
			SokobanResult result = new SokobanResult(person, score);
			highscoreList.addResult(result);
		}
	}
	
	public void run() {
		setSize(200, 250);
		setVisible(true);
		while (true) {
			addScore();
		}
	}
	
	public void addScore() {
		String name = readLine("Name: ");
		int moves = readInt("Moves: ");
		SokobanResult result = new SokobanResult(name, moves);
		highscoreList.addResult(result);
	}
	
	
	@Override
	public void listChanged(ObservableList listChanged, int lowestIndex, int highestIndex) {
		if (listChanged instanceof HighscoreList) {
			removeAll();
			Iterator<Comparable> it = ((HighscoreList) listChanged).iterator();
			int count = 1;
			int width = 10;
			int height = 20;
			while (it.hasNext()) {
				SokobanResult res = (SokobanResult) it.next();
				GLabel label = new GLabel(count + ": " + res.toString(), width, height);
				count++;
				height += 20;
				add(label);
				
			}
		}
	}
	
}
