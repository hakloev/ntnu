package oving4;

import javax.swing.*;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.beans.PropertyChangeEvent;
import java.beans.PropertyChangeListener;
import java.beans.PropertyChangeSupport;

/**
 * Created by hakloev on 22/01/14.
 */
public class PersonPanel extends JPanel implements PropertyChangeListener {
	
	protected JLabel nameLabel, emailLabel, birthdayLabel, genderLabel, heightLabel;
	protected JTextField NamePropertyComponent, EmailPropertyComponent, DateOfBirthPropertyComponent;
	protected JComboBox<Gender> GenderPropertyComponent;
	protected JSlider HeightPropertyComponent;

	private final Dimension textFieldDimension = new Dimension(320, 20);
	private final Dimension sliderDimension = new Dimension(320, 40);
	private final int guiElementSpacing = 5;
	private final int heightSliderMin = 120;
	private final int heightSliderMax = 220;
	private final int heightSliderInit = 170;

	protected Person model;

	public PersonPanel() {
		initGUI();
		initLayout();
		this.model = null;
	}

	private void initGUI() {
		nameLabel = new JLabel("Name:");
		emailLabel = new JLabel("Email:");
		birthdayLabel = new JLabel("Birthday:");
		genderLabel = new JLabel("Gender:");
		heightLabel = new JLabel("Height:");

		NamePropertyComponent = new JTextField();
		NamePropertyComponent.setPreferredSize(textFieldDimension);
		NamePropertyComponent.addActionListener(new NameFieldChanged());
		EmailPropertyComponent = new JTextField();
		EmailPropertyComponent.setPreferredSize(textFieldDimension);
		EmailPropertyComponent.addActionListener(new EmailFieldChanged());
		DateOfBirthPropertyComponent = new JTextField();
		DateOfBirthPropertyComponent.setPreferredSize(textFieldDimension);
		DateOfBirthPropertyComponent.addActionListener(new BirthdayFieldChanged());

		GenderPropertyComponent = new JComboBox<Gender>();
		GenderPropertyComponent.addItem(Gender.male);
		GenderPropertyComponent.addItem(Gender.female);
		GenderPropertyComponent.addActionListener(new GenderFieldChanged());

		HeightPropertyComponent = new JSlider(JSlider.HORIZONTAL,
				heightSliderMin, heightSliderMax, heightSliderInit);
		HeightPropertyComponent.setPreferredSize(sliderDimension);
		HeightPropertyComponent.setMajorTickSpacing(10);
		HeightPropertyComponent.setMinorTickSpacing(1);
		HeightPropertyComponent.setPaintTicks(true);
		HeightPropertyComponent.setPaintLabels(true);
		HeightPropertyComponent.addChangeListener(new SliderChangedListener());

		NamePropertyComponent.setName("NamePropertyComponent");
		EmailPropertyComponent.setName("EmailPropertyComponent");
		DateOfBirthPropertyComponent.setName("DateOfBirthPropertyComponent");
		GenderPropertyComponent.setName("GenderPropertyComponent");
		HeightPropertyComponent.setName("HeightPropertyComponent");

		add(nameLabel);
		add(emailLabel);
		add(birthdayLabel);
		add(genderLabel);
		add(heightLabel);

		add(NamePropertyComponent);
		add(EmailPropertyComponent);
		add(DateOfBirthPropertyComponent);
		add(GenderPropertyComponent);
		add(HeightPropertyComponent);
	}

	private void initLayout() {
		SpringLayout layout = new SpringLayout();
		setLayout(layout);

		// putConstraint(hvilken grense, hvilken komponent, avstand (piksel), iforhold til komponent, komponent)

		// Fix constraints for nameLabel and nameProperty
		layout.putConstraint(SpringLayout.WEST, nameLabel, guiElementSpacing, SpringLayout.WEST, this);
		layout.putConstraint(SpringLayout.NORTH, nameLabel, 7, SpringLayout.NORTH, this);

		layout.putConstraint(SpringLayout.WEST, NamePropertyComponent, 20, SpringLayout.EAST, nameLabel);
		layout.putConstraint(SpringLayout.NORTH, NamePropertyComponent, guiElementSpacing, SpringLayout.NORTH, this);

		// Fix constraints for emailLabel and emailProperty
		layout.putConstraint(SpringLayout.WEST, emailLabel, guiElementSpacing, SpringLayout.WEST, this);
		layout.putConstraint(SpringLayout.NORTH, emailLabel, 10, SpringLayout.SOUTH, nameLabel);

		layout.putConstraint(SpringLayout.WEST, EmailPropertyComponent, 22, SpringLayout.EAST, emailLabel);
		layout.putConstraint(SpringLayout.NORTH, EmailPropertyComponent, -2, SpringLayout.NORTH, emailLabel);

		// Fix constraints for birthdayLabel og dateOfBirthProperty
		layout.putConstraint(SpringLayout.WEST, birthdayLabel, guiElementSpacing, SpringLayout.WEST, this);
		layout.putConstraint(SpringLayout.NORTH, birthdayLabel, 10, SpringLayout.SOUTH, emailLabel);

		layout.putConstraint(SpringLayout.WEST, DateOfBirthPropertyComponent, 5, SpringLayout.EAST, birthdayLabel);
		layout.putConstraint(SpringLayout.NORTH, DateOfBirthPropertyComponent, 7, SpringLayout.SOUTH, EmailPropertyComponent);

		// Fix constraints for genderLabel and GenderProperty
		layout.putConstraint(SpringLayout.WEST, genderLabel, guiElementSpacing, SpringLayout.WEST, this);
		layout.putConstraint(SpringLayout.NORTH, genderLabel, 13, SpringLayout.SOUTH, birthdayLabel);

		layout.putConstraint(SpringLayout.WEST, GenderPropertyComponent, 12, SpringLayout.EAST, genderLabel);
		layout.putConstraint(SpringLayout.NORTH, GenderPropertyComponent, guiElementSpacing, SpringLayout.SOUTH, DateOfBirthPropertyComponent);

		// Fix constraints for heightLabel and HeightProperty
		layout.putConstraint(SpringLayout.WEST, heightLabel, guiElementSpacing, SpringLayout.WEST, this);
		layout.putConstraint(SpringLayout.NORTH, heightLabel, 22, SpringLayout.SOUTH, genderLabel);

		layout.putConstraint(SpringLayout.WEST, HeightPropertyComponent, 12, SpringLayout.EAST, heightLabel);
		layout.putConstraint(SpringLayout.NORTH, HeightPropertyComponent, guiElementSpacing, SpringLayout.SOUTH, GenderPropertyComponent);
	}

	public void setModel(Person p) {
		if (model != null) {
			model.removePropertyChangeListener(this);
		}
        if (p != null) {
	        this.model = p;
			System.out.println("Controller added listener to model " + p.getName());
	        model.addPropertyChangeListener(this);
	        NamePropertyComponent.setText(model.getName());
	        EmailPropertyComponent.setText(model.getEmail());
	        DateOfBirthPropertyComponent.setText(model.getDateOfBirth());
	        GenderPropertyComponent.setSelectedItem(model.getGender());
	        HeightPropertyComponent.setValue(model.getHeight());
        }
	}

	public Person getModel() {
		return this.model;
	}

	public void clearAll() {
		NamePropertyComponent.setText("");
		EmailPropertyComponent.setText("");
		DateOfBirthPropertyComponent.setText("");
		GenderPropertyComponent.setSelectedIndex(-1);
		HeightPropertyComponent.setValue(120);
	}

    @Override
    public void propertyChange(PropertyChangeEvent evt) {
        System.out.println("Property changed in model " + model.getName() + ", recieved firePropertyChanged, change view");
        if (evt.getPropertyName() == Person.NAME_PROP) {
            NamePropertyComponent.setText(model.getName());
        } else if (evt.getPropertyName() == Person.BIRTHDAY_PROP) {
            DateOfBirthPropertyComponent.setText(model.getDateOfBirth());
        } else if (evt.getPropertyName() == Person.EMAIL_PROP) {
            EmailPropertyComponent.setText(model.getEmail());
        } else if (evt.getPropertyName() == Person.GENDER_PROP) {
            GenderPropertyComponent.setSelectedItem(model.getGender());
        } else if (evt.getPropertyName() == Person.HEIGHT_PROP) {
            HeightPropertyComponent.setValue(model.getHeight());
        }
    }

    // Kan ha en listener for alle felt, men vil da oppnå unødvendige endringer, og mye ressursbruk

    private class NameFieldChanged implements ActionListener {

        @Override
        public void actionPerformed(ActionEvent e) {
	        if (model != null) {
		        model.setName(NamePropertyComponent.getText());
	        }
        }
    }

    private class EmailFieldChanged implements ActionListener {

        @Override
        public void actionPerformed(ActionEvent e) {
	        if (model != null) {
		        model.setEmail(EmailPropertyComponent.getText());
	        }
        }
    }

    private class BirthdayFieldChanged implements ActionListener {

        @Override
        public void actionPerformed(ActionEvent e) {
	        if (model != null) {
		        model.setDateOfBirth(DateOfBirthPropertyComponent.getText());
	        }
        }
    }

    private class GenderFieldChanged implements ActionListener {

        @Override
        public void actionPerformed(ActionEvent e) {
	        if (model != null) {
		        model.setGender((Gender) GenderPropertyComponent.getSelectedItem());
	        }
        }
    }

    private class SliderChangedListener implements ChangeListener {

        @Override
        public void stateChanged(ChangeEvent e) {
	        if (model != null) {
		        model.setHeight(HeightPropertyComponent.getValue());
	        }
        }

    }
}
