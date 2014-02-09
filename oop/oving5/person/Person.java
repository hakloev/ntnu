package oving5.person;

import java.util.ArrayList;

public class Person {
	
	// Instance fields
	private String name;
	private char gender;
	private Person mother;
	private Person father;
	private ArrayList<Person> children;
	
	/**
	 * Constructor
	 * @param gender
	 */
	public Person(char gender) {
		if ((gender == 'm') || (gender == 'f')) { // validate gender
			this.gender = gender;
		}
		children = new ArrayList<Person>(); // initialice children-list
	}
	
	/**
	 * check if person is male
	 * @return boolean
	 */
	public boolean isMale() {
		if (this.gender == 'm') {
			return true;
		}
		return false;
	}
	
	/**
	 * same as isMale
	 * @return boolean
	 */
	public boolean isFemale() {
		if (this.gender == 'f') {
			return true;
		}
		return false;
	}
	
	/**
	 * sets name if valid name
	 * @param name
	 */
	public void setName(String name) {
		for (int i = 0; i < name.length(); i++) {
			if (!(Character.isLetter(name.charAt(i)) || (name.charAt(i) == ' '))) { // check input
				return;
			}
		}
		this.name = name;
	}
	
	/**
	 * returns name
	 * @return this.name
	 */
	public String getName() {
		return this.name;
	}
	
	/**
	 * returns number of children
	 * @return this.children.size()
	 */
	public int getChildCount() {
		return this.children.size();
	}
	
	/**
	 * return mother
	 * @return this.mother
	 */
	public Person getMother() {
		return this.mother;
	}
	
	/**
	 * opposite of getMother
	 * @return this.father
	 */
	public Person getFather() {
		return this.father;
	}
	
	/**
	 * sets mother, check relations, deletes previous relations
	 * @param motherOf
	 */
	public void setMother(Person motherOf) {
		if (motherOf != null) { // check if mother ain't null
			if (motherOf.gender != 'f') { // validate that parameter is female
				return; // not female, returns
			} else { // parameter is female
				if (this.mother != null) { // if this.mother ain't null we must remove previous this from previous mother
					this.mother.children.remove(this); // 
				}
				
				if (motherOf.children.contains(this)) { // if this is in motherOf children list we set this.mother to motherOf
					this.mother = motherOf;
				} else { // if not, we set this.mother to motherOf and add this to motherOfs childrenlist
					motherOf.children.add(this);
					this.mother = motherOf;
				}
			} 
		} else { // motherOf is null
			if (this.mother != null) { // if this.mother ain't null
				this.mother.children.remove(this); // remove this from mothers childrenlist
				this.mother = null; // set this.mother to null
			}
		}
	}
	
	public void setFather(Person fatherOf) {
		// identical to setMother, check comments there
		if (fatherOf != null) {
			if (fatherOf.gender != 'm') {
				return;
			} else {
				if (this.father != null) {
					this.father.children.remove(this);
				}
				
				if (fatherOf.children.contains(this)) {
					this.father = fatherOf;
				} else {
					fatherOf.children.add(this);
					this.father = fatherOf;
				}
			} 
		} else {
			if (this.father != null) {
				this.father.children.remove(this);
				this.father = null;
			} 
		}
	}
	
	/**
	 * addChild to children list
	 * @param child
	 */
	public void addChild(Person child) {
		if (!this.children.contains(child)) { // if not in this children list, we add child
			this.children.add(child); 
			switch (this.gender) { // depending on this gender, we choose setFather or setMother
				case 'm': child.setFather(this); break;
				case 'f': child.setMother(this); break;
			}
		}
	}
	
	/**
	 * removeChild from this children list
	 * @param child
	 */
	public void removeChild(Person child) {
		if (this.children.contains(child)) { // if child in this children list, we remove child
			this.children.remove(child); 
			switch (this.gender) { // setFather and Mother depending on this gender
				case 'm': child.setFather(null); break;
				case 'f': child.setMother(null); break;
			}
		}
		
	}
	
	/**
	 * return child on given index, if valid index
	 * @param index
	 * @return child
	 */
	public Person getChild(int index) {
		if ((index >= 0) && (index < this.children.size())) {
			return this.children.get(index);
		}
		return null;
	}
	
	/**
	 * returns index of child, if it is in children list, else -1 as default
	 * @param child
	 * @return index
	 */
	public int indexOfChild(Person child) {
		if (this.children.contains(child)) {
			return this.children.indexOf(child);
		} else {
			return -1;
		}
	}
	
	/**
	 * if child in list, return boolean
	 * @param child
	 * @return boolean
	 */
	public boolean containsChild(Person child) {
		if (this.children.contains(child)) {
			return true;
		}
		return false;
	}
	
	/**
	 * check if parameter person is ancestor of Person c (a child from child list)
	 * @param person
	 * @return boolean
	 */
	public boolean isAncestorOf(Person person) {
		for (Person c : this.children) { // iterate over all this.children persons
			if (c == person) { // true if child equals person
				return true;
			} else if (c.isAncestorOf(person)) { // if not, call isAncestorOf on child
				return true;
			}
		}
		return false;
	}
	
}
