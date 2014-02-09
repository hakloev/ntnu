package oving9;

import java.util.ArrayList;
import java.util.List;

public abstract class ObservableList {
	
	private List<ListListener> listenersList;
	
	public ObservableList() {
		listenersList = new ArrayList<ListListener>();
	}
	
	public void addListListener(ListListener toBeAdded) {
		if (!(listenersList.contains(toBeAdded))) {
			listenersList.add(toBeAdded);
		}
	}
	
	public void removeListListener(ListListener toBeRemoved) {
		if (listenersList.contains(toBeRemoved)) {
			listenersList.remove(toBeRemoved);
		}
	}
	
	protected void fireListChanged(int lowestIndex, int highestIndex) {
		for (int i = 0; i < listenersList.size(); i++) {
			listenersList.get(i).listChanged(this, lowestIndex, highestIndex);
		}
	}
	
	@SuppressWarnings("rawtypes")
	protected abstract List getList(); 
	
	public int size() {
		return this.getList().size();
	}
	
	@SuppressWarnings("unchecked")
	protected void addElement(int index, Object element) {
		this.getList().add(index, element);
//		System.out.println(index + " " + this.getList().size());
		fireListChanged(index, this.getList().size() - 1);
	}
	
	protected void removeElement(int index) {
		this.getList().remove(index);
		fireListChanged(index, this.getList().size());
	}
	
}
