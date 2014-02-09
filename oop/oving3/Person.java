package oving3;

import java.util.ArrayList;
import acm.program.ConsoleProgram;

public class Person extends ConsoleProgram {
	// Lager fire felt til klassen, og initialiserer arraylista med engang
	String name;
	Person mother;
	Person father;
	ArrayList<Person> children = new ArrayList<Person>();
	
	public Person() {
		
	}
	
	/**
	 * Konstruktør som tar inn navn ved opprettelse av et objekt
	 * @param name
	 */
	public Person(String name) {
		this.name = name; // Setter navnet på objektet som det jobbes på til name
	}
	
	/**
	 * 	Konstruktør som tar inn navn, far-objekt og mor objekt
	 * @param name
	 * @param father
	 * @param mother
	 */
	public Person(String name, Person father, Person mother) {
		this.name = name; // Setter navn på objektet vi jobber med til name
		this.father = father; // Setter father på this til Person father
		this.mother = mother; // Setter mother på this til Person mother
		this.father.children.add(this); // Legger til this i children-lista til this.father
		this.mother.children.add(this); // Legger til this i children-lista til this.mother
	}

	/**
	 * isMotherOf-metode, tar inn person-objekt og sjekker om det ligger i children-lista
	 * til objektet vi arbeider på
	 * Sjekker også om navnet til objektet vi jobber på er det samme som navnet til moren til 
	 * person-parameteret
	 * @param person
	 * @return boolean
	 */
	public boolean isMotherOf(Person person) {
		if ((this.children.contains(person)) && (this.name.equals(person.mother.name))) {
			return true;
		}
		return false;
	}
	
	/**
	 * isFatherOf-metode, tar inn person-objekt og sjekker om det ligger i children-lista
	 * til objektet vi arbeider på 
	 * Sjekker også om navnet til objektet vi jobber på er det samme som navnet til faren til 
	 * person-parameteret
	 * @param person
	 * @return boolean
	 */
	public boolean isFatherOf(Person person) {
		if ((this.children.contains(person)) && (this.name.equals(person.father.name))) {
			return true;
		}
		return false;
	}
	
	/**
	 * isSiblingOf-meotde, tar inn person-objekt og sjekker om det er fullstendig søsken til 
	 * objektet vi arbeider på
	 * @param person
	 * @return boolean
	 */
	public boolean isSiblingOf(Person person) {
		if ((this.mother.name.equals(person.mother.name)) && (this.father.name.equals(person.father.name))) {
			if (!this.name.equals(person.name)) {
				return true;				
			}
		}
		return false;
	}	

	/**
	 * toString-metode som returnerer en liste over familierelasjoner avhengig av 
	 * hva som er tilgjengelig av informasjon i objektet
	 * @return string
	 */
	public String toString() {
		String childStr = "";
		if (((this.father == null) && (this.mother == null)) && (!this.children.isEmpty())) {
			for (int i = 0; i < this.children.size(); i++) {
				if (i == 0) {
					childStr += this.children.get(i).name;
				} else if (i == (this.children.size() - 1)) {
					childStr += " and " + this.children.get(i).name;					
				} else {
					childStr += ", " + this.children.get(i).name;
				}
			} 
			return "Object: " + this.name + "\nDoesn't have any parents!\n" + this.name + "'s children are " + childStr + "\n";
		} else if (((this.father != null) && (this.mother != null)) && (!this.children.isEmpty())) {
			for (int i = 0; i < this.children.size(); i++) {
				if (i == 0) {
					childStr += this.children.get(i).name;
				} else if (i == (this.children.size() - 1)) {
					childStr += " and " + this.children.get(i).name;
				} else {
					childStr += ", " + this.children.get(i).name;										
				}
			}
			return "Object: " + this.name + "\nFather: " + this.father.name + "\nMother: " + this.mother.name + "\n" + this.name + "'s children are " + childStr + "\n";
		} else if (((this.father != null) && (this.mother != null)) && (this.children.isEmpty())) {
			return "Object: " + this.name + "\nFather: " + this.father.name + "\nMother: " + this.mother.name + "\n" + this.name + " has no children\n";
		} else {
			return "Something went wrong, this person called" + this.name + " is apperantly not in the royal family!";
		}
	}
}