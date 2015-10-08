package oving2;

import java.awt.Dimension;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JSlider;
import javax.swing.JTextField;
import javax.swing.SpringLayout;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;


public class PersonPanel extends JPanel {
	
	private JLabel nameLabel, emailLabel, birthdayLabel, genderLabel, heightLabel;
	private JTextField NamePropertyComponent, EmailPropertyComponent, DateOfBirthPropertyComponent;
	private JComboBox<Gender> GenderPropertyComponent;
	private JSlider HeightPropertyComponent;
	
	private final Dimension textFieldDimension = new Dimension(320, 20);
	private final Dimension sliderDimension = new Dimension(320, 40);
	private final int guiElementSpacing = 5;
	private final int heightSliderMin = 120;
	private final int heightSliderMax = 220;
	private final int heightSliderInit = 170;
	
	private Person model;
	
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
		
		TextFieldsChanged textFieldChangedListener = new TextFieldsChanged();
		
		NamePropertyComponent = new JTextField();
		NamePropertyComponent.setPreferredSize(textFieldDimension);
		NamePropertyComponent.addActionListener(textFieldChangedListener);
		EmailPropertyComponent = new JTextField();
		EmailPropertyComponent.setPreferredSize(textFieldDimension);
		EmailPropertyComponent.addActionListener(textFieldChangedListener);
		DateOfBirthPropertyComponent = new JTextField();
		DateOfBirthPropertyComponent.setPreferredSize(textFieldDimension);
		DateOfBirthPropertyComponent.addActionListener(textFieldChangedListener);
		
		GenderPropertyComponent = new JComboBox<Gender>();
		GenderPropertyComponent.addItem(Gender.male);
		GenderPropertyComponent.addItem(Gender.female);
		GenderPropertyComponent.addActionListener(textFieldChangedListener);
		
		HeightPropertyComponent = new JSlider(JSlider.HORIZONTAL, 
				heightSliderMin, heightSliderMax, heightSliderInit);
		HeightPropertyComponent.setPreferredSize(sliderDimension);
		HeightPropertyComponent.setMajorTickSpacing(10);
		HeightPropertyComponent.setMinorTickSpacing(1);
		HeightPropertyComponent.setPaintTicks(true);
		HeightPropertyComponent.setPaintLabels(true);
		HeightPropertyComponent.addChangeListener(new SliderChangedListner());
		
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
		this.model = p;
		NamePropertyComponent.setText(model.getName());
		EmailPropertyComponent.setText(model.getEmail());
		DateOfBirthPropertyComponent.setText(model.getDateOfBirth());
		GenderPropertyComponent.setSelectedItem(model.getGender());
		HeightPropertyComponent.setValue(model.getHeight());
	}
	
	public Person getModel() {
		return this.model;
	}
	
	private class SliderChangedListner implements ChangeListener {

		@Override
		public void stateChanged(ChangeEvent e) {
			model.setHeight(HeightPropertyComponent.getValue());
		}
		
	}
	
	private class TextFieldsChanged implements ActionListener {

		@Override
		public void actionPerformed(ActionEvent e) {
			model.setName(NamePropertyComponent.getText());
			model.setEmail(EmailPropertyComponent.getText());
			model.setDateOfBirth(DateOfBirthPropertyComponent.getText());
			model.setGender((Gender) GenderPropertyComponent.getSelectedItem());
		}
		
	}
	
	public static void main(String[] args) {
		JFrame frame = new JFrame("Øving T2");
		PersonPanel panel = new PersonPanel();
		panel.setModel(new Person("Håkon Løvdal"));
		frame.setContentPane(panel);
		frame.setPreferredSize(new Dimension(390, 190));
		frame.pack();
		frame.setVisible(true);
		
	}
}
