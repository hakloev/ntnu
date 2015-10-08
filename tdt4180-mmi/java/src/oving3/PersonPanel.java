package oving3;

import javax.swing.*;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.beans.PropertyChangeEvent;
import java.beans.PropertyChangeListener;

/**
 * Created by hakloev on 22/01/14.
 */
public class PersonPanel extends JPanel implements PropertyChangeListener {
	
	protected JLabel nameLabel, emailLabel, birthdayLabel, genderLabel, heightLabel;
	protected JTextField NamePropertyComponent, EmailPropertyComponent, DateOfBirthPropertyComponent;
	protected JComboBox<Gender> GenderPropertyComponent;
	protected JSlider HeightPropertyComponent;

	protected SpringLayout layout;

	protected final Dimension textFieldDimension = new Dimension(320, 20);
	private final Dimension sliderDimension = new Dimension(320, 40);
	protected final int guiElementSpacing = 5;
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
		NamePropertyComponent.addKeyListener(new NameFieldChanged());
		EmailPropertyComponent = new JTextField();
		EmailPropertyComponent.setPreferredSize(textFieldDimension);
		EmailPropertyComponent.addKeyListener(new EmailFieldChanged());
		DateOfBirthPropertyComponent = new JTextField();
		DateOfBirthPropertyComponent.setPreferredSize(textFieldDimension);
		DateOfBirthPropertyComponent.addKeyListener(new BirthdayFieldChanged());

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
		layout = new SpringLayout();
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
		this.model = p;
        System.out.println("Controller added listner to model");
        model.addPropertyChangeListener(this);
		NamePropertyComponent.setText(model.getName());
		EmailPropertyComponent.setText(model.getEmail());
		DateOfBirthPropertyComponent.setText(model.getDateOfBirth());
		GenderPropertyComponent.setSelectedItem(model.getGender());
		HeightPropertyComponent.setValue(model.getHeight());
	}

	public Person getModel() {
		return this.model;
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
            GenderPropertyComponent.setSelectedItem(model.getGender());
        } else if (evt.getPropertyName() == Person.HEIGHT_PROP) {
            HeightPropertyComponent.setValue(model.getHeight());
        }
    }

    // Kan ha en listener for alle felt, men vil da oppnå unødvendige endringer, og mye ressursbruk

    private class NameFieldChanged implements KeyListener {

	    @Override
	    public void keyTyped(KeyEvent e) {

	    }

	    @Override
	    public void keyPressed(KeyEvent e) {

	    }

	    @Override
	    public void keyReleased(KeyEvent e) {
		    model.setName(NamePropertyComponent.getText());
	    }
    }

	private class EmailFieldChanged implements KeyListener {

		@Override
		public void keyTyped(KeyEvent e) {

		}

		@Override
		public void keyPressed(KeyEvent e) {

		}

		@Override
		public void keyReleased(KeyEvent e) {
			model.setEmail(EmailPropertyComponent.getText());
		}
	}


	private class BirthdayFieldChanged implements KeyListener {

		@Override
		public void keyTyped(KeyEvent e) {

		}

		@Override
		public void keyPressed(KeyEvent e) {

		}

		@Override
		public void keyReleased(KeyEvent e) {
			model.setDateOfBirth(DateOfBirthPropertyComponent.getText());
		}
	}


	private class GenderFieldChanged implements ActionListener {

        @Override
        public void actionPerformed(ActionEvent e) {
            model.setGender((Gender) GenderPropertyComponent.getSelectedItem());
        }
    }

    private class SliderChangedListener implements ChangeListener {

        @Override
        public void stateChanged(ChangeEvent e) {
            model.setHeight(HeightPropertyComponent.getValue());
        }

    }

	public static void main(String[] args) {
		JFrame frame = new JFrame("Øving T3");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel container = new JPanel();
        container.setLayout(new BoxLayout(container, BoxLayout.X_AXIS));

        Person p = new Person();
        PersonPanel panel = new PersonPanel();
        PassivePersonClass panel1 = new PassivePersonClass();

        panel.setModel(p);
        panel1.setModel(p);

        container.add(panel);
        container.add(panel1);

        frame.setContentPane(container);
		frame.setPreferredSize(new Dimension((395*2), 190));
        frame.setVisible(true);
		frame.pack();
    }
}
