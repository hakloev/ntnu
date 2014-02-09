package oving9;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class HighscoreList extends ObservableList implements Iterable<Comparable> {

	private int maxSize;
	private List<Comparable> highscores;
	
	public HighscoreList(int maxSize) {
		this.maxSize = maxSize;
		highscores = new ArrayList<Comparable>(); 
	}
	
	public void addResult(Comparable element) {
//		System.out.println("works");
//		System.out.println(element.toString());
		if (highscores.size() == 0) {
//			System.out.println("tada0");
			addElement(0, element);
		} else if (highscores.size() < maxSize) {
//			System.out.println("tada");
			for (int i = 0; i < highscores.size(); i++) {
				if (element.compareTo(highscores.get(i)) <= 0) {
//					System.out.println("tada1");
					addElement(i, element);
					return;
				} else if (i == highscores.size() - 1) {
//					System.out.println("tada2");
					addElement(i + 1, element);
					return;
				}
			}
		} else if (highscores.size() == maxSize) {
//			System.out.println("tada3");
			for (int i = 0; i < highscores.size(); i++) {
				if (element.compareTo(highscores.get(i)) <= 0) {
//					System.out.println("tada4");
					highscores.remove(maxSize - 1);
					addElement(i, element);
					return; 
				} 
			}
		}
	}

	@Override
	protected List getList() {
		return this.highscores;
	}

	@Override
	public Iterator<Comparable> iterator() {
		return this.getList().iterator();
	}

}
