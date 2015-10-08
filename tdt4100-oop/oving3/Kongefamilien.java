package oving3;

import java.util.ArrayList; 
import acm.program.ConsoleProgram;

public class Kongefamilien extends ConsoleProgram {
	// Initaliserer en ArrayList kongefamilien 
	ArrayList<Person> kongefamilien = new ArrayList<Person>();
	
	public void init() {

	}
	
	public void run() {
		setSize(550, 650); // Setter størrelsen på applet-window til 550 x og 650 y
		createRoyalFamily(); // Kaller createRoyalFamily-metoden
	}
	
	/** 
	 * createRoyalFamily-metode, for hva den gjør se i metoden
	 * @return void
	 */
	public void createRoyalFamily() {
		// Genererer et personobjekt for hvert familiemedlem og legger det til i "kongefamilien"
		// Konge og dronning
		Person harald = new Person("Harald"); // Lager et person objekt harald
		kongefamilien.add(harald); // Legger objektet harald til i "kongefamilien"
		Person sonja = new Person("Sonja");
		kongefamilien.add(sonja);
		
		// Prins og prinsesse 
		Person haakon = new Person("Haakon", harald, sonja);
		kongefamilien.add(haakon);
		Person martha = new Person("Märtha", harald, sonja);
		kongefamilien.add(martha);
		
		// Inngifte 
		Person mette = new Person("Mette-Marit");
		kongefamilien.add(mette);
		Person ari = new Person("Ari-Behn");
		kongefamilien.add(ari);
		
		// Barn av prins og prinsesse
			// Haakon og Mette-Marit
			Person ingrid = new Person("Ingrid Alexandra", haakon, mette);
			kongefamilien.add(ingrid);
			Person sverre = new Person("Sverre Magnus", haakon, mette);
			kongefamilien.add(sverre);
		
			// Märtha og Ari-Behn
			Person maud = new Person("Maud Angelica", ari, martha);
			kongefamilien.add(maud);
			Person leah = new Person("Leah Isadora", ari, martha);
			kongefamilien.add(leah);
			Person emma = new Person("Emma-Tallulah", ari, martha);
			kongefamilien.add(emma);
		
		// Printer samtlige objekter med relasjoner via for-løkke 
		for (Person p : kongefamilien) {
			println(p); // Benytter meg av syntaks-sukker og printer via toString-metoden
		}
	}
}
