package oving3;

import javax.swing.*;
import java.beans.PropertyChangeEvent;

/**
 * Created by hakloev on 22/01/14.
 */
public class PassivePersonClass extends PersonPanel {

	private JTextField NewGenderTextField;
	private JTextField NewHeightTextField;

    public PassivePersonClass() {
	    super();
	    remove(GenderPropertyComponent);
	    remove(HeightPropertyComponent);
	    NewGenderTextField = new JTextField();
	    NewHeightTextField = new JTextField();
	    NewGenderTextField.setPreferredSize(textFieldDimension);
	    NewHeightTextField.setPreferredSize(textFieldDimension);

	    fixLayout();

	    add(NewGenderTextField);
	    add(NewHeightTextField);

	    setEditable(false);
    }

    public void setEditable(boolean b) {
        super.NamePropertyComponent.setEditable(b);
        super.DateOfBirthPropertyComponent.setEditable(b);
        super.EmailPropertyComponent.setEditable(b);
		NewGenderTextField.setEditable(b);
	    NewHeightTextField.setEditable(b);
    }

	private void fixLayout() {
		layout.putConstraint(SpringLayout.WEST, NewGenderTextField, 12, SpringLayout.EAST, genderLabel);
		layout.putConstraint(SpringLayout.NORTH, NewGenderTextField, 7, SpringLayout.SOUTH, DateOfBirthPropertyComponent);

		layout.putConstraint(SpringLayout.WEST, NewHeightTextField, 14, SpringLayout.EAST, heightLabel);
		layout.putConstraint(SpringLayout.NORTH, NewHeightTextField, 20, SpringLayout.SOUTH, NewGenderTextField);
	}

	@Override
	public void propertyChange(PropertyChangeEvent evt) {
		System.out.println("Property changed in model, recieved firePropertyChanged, change view");
		if (evt.getPropertyName() == Person.NAME_PROP) {
			NamePropertyComponent.setText(model.getName());
		} else if (evt.getPropertyName() == Person.BIRTHDAY_PROP) {
			DateOfBirthPropertyComponent.setText(model.getDateOfBirth());
		} else if (evt.getPropertyName() == Person.EMAIL_PROP) {
			EmailPropertyComponent.setText(model.getEmail());
		} else if (evt.getPropertyName() == Person.GENDER_PROP) {
			NewGenderTextField.setText(super.model.getGender().toString());
		} else if (evt.getPropertyName() == Person.HEIGHT_PROP) {
			NewHeightTextField.setText(String.valueOf(super.model.getHeight()));
		}
	}

	@Override
	public void setModel(Person p) {
		model = p;
		System.out.println("Controller added listner to model");
		model.addPropertyChangeListener(this);
		NamePropertyComponent.setText(model.getName());
		EmailPropertyComponent.setText(model.getEmail());
		DateOfBirthPropertyComponent.setText(model.getDateOfBirth());
		if (model.getGender() != null) {
			NewGenderTextField.setText(model.getGender().toString());
		}
		NewHeightTextField.setText(String.valueOf(model.getHeight()));
	}
}

