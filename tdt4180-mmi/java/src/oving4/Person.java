package oving4;

import com.sun.java.swing.plaf.motif.resources.motif;

import java.beans.PropertyChangeListener;
import java.beans.PropertyChangeSupport;

/**
 * Created by hakloev on 22/01/14.
 */
public class Person {

    public final static String NAME_PROP = "NAME";
    public final static String BIRTHDAY_PROP = "BIRTHDAY";
    public final static String GENDER_PROP = "GENDER";
    public final static String EMAIL_PROP = "EMAIL";
    public final static String HEIGHT_PROP = "HEIGHT";

    private String name;
	private String dateOfBirth;
	private Gender gender;
	private String email;
	private int height;

    private final PropertyChangeSupport pcs;

	public Person() {
		pcs = new PropertyChangeSupport(this);
		System.out.println("Created pcs in model0");
	}

	public Person(String name) {
        pcs = new PropertyChangeSupport(this);
        System.out.println("Created pcs in model1 " + name);
        this.name = name;
    }

	@Override
	public String toString() {
		return "Name: " + name + " Email: " + email;
	}

    public void addPropertyChangeListener(PropertyChangeListener listener) {
        System.out.println("Model " + getName() + " added listener from controller");
        pcs.addPropertyChangeListener(listener);
    }

	public void removePropertyChangeListener(PropertyChangeListener listener) {
		System.out.println("Model " + getName() + " removed listener from controller");
		pcs.removePropertyChangeListener(listener);
	}

	public void setName(String name) {
        String oldValue = this.name;
        this.name = name;
        pcs.firePropertyChange(NAME_PROP, oldValue, name);
    }

	public void setDateOfBirth(String dateOfBirth) {
        String oldValue = this.dateOfBirth;
		this.dateOfBirth = dateOfBirth;
        pcs.firePropertyChange(BIRTHDAY_PROP, oldValue, dateOfBirth);
	}

	public void setGender(Gender gender) {
        Gender oldValue = this.gender;
		this.gender = gender;
        pcs.firePropertyChange(GENDER_PROP, oldValue, gender);
	}

	public void setEmail(String email) {
        String oldValue = this.email;
	    this.email = email;
        pcs.firePropertyChange(EMAIL_PROP, oldValue, gender);
    }

	public void setHeight(int height) {
        int oldValue = this.height;
		this.height = height;
        pcs.firePropertyChange(HEIGHT_PROP, oldValue, height);
	}

    public String getName() {
        return name;
    }

    public String getDateOfBirth() {
        return dateOfBirth;
    }

    public Gender getGender() {
        return gender;
    }

    public int getHeight() {
        return height;
    }

    public String getEmail() {
        return email;
    }

}