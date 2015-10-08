package oving4;

import javax.swing.*;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class PersonListPanel extends JPanel implements ListSelectionListener {

    private JList<Person> PersonList;
	private JScrollPane ScrollPane;
    private PersonPanel PersonPanel;
    private JButton AddPerson;
    private JButton RemovePerson;

    private DefaultListModel<Person> listModel;

    public PersonListPanel() {
        PersonList = new JList<Person>();
	    ScrollPane = new JScrollPane(PersonList);
        PersonPanel = new PersonPanel();
        AddPerson = new JButton("Add person");
        RemovePerson = new JButton("Remove person");

        PersonList.addListSelectionListener(this);
	    PersonList.setCellRenderer(new PersonRenderer());
	    PersonList.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
	    setModel(new DefaultListModel<Person>());

	    AddPerson.addActionListener(new AddPersonListener());
        RemovePerson.addActionListener(new RemovePersonListener());

	    PersonList.setName("PersonList");
	    PersonPanel.setName("PersonPanel");
	    AddPerson.setName("NewPersonButton");
	    RemovePerson.setName("DeletePersonButton");

        initGUI();
        initLayout();
    }

    private void initGUI() {
        PersonList.setPreferredSize(new Dimension(200, 200));
        PersonPanel.setPreferredSize(new Dimension(400, 200));
        AddPerson.setPreferredSize(new Dimension(100, 20));
        RemovePerson.setPreferredSize(new Dimension(100, 20));
    }

    private void initLayout() {
        setLayout(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.fill = GridBagConstraints.VERTICAL;
        gbc.gridx = 0;
        gbc.gridy = 0;
        add(ScrollPane, gbc);

        gbc.gridx = 1;
        add(PersonPanel, gbc);

        gbc.fill = GridBagConstraints.BOTH;
        gbc.gridx = 0;
        gbc.gridy = 1;
        add(AddPerson, gbc);
        gbc.gridx = 1;
        add(RemovePerson, gbc);
    }

    public void setModel(DefaultListModel<Person> model) {
        this.listModel = model;
        PersonList.setModel(listModel);
    }

    public DefaultListModel<Person> getModel() {
        return this.listModel;
    }

	@Override
	public void valueChanged(ListSelectionEvent e) {
		PersonPanel.setModel(PersonList.getSelectedValue());
	}

	private class AddPersonListener implements ActionListener {

        @Override
        public void actionPerformed(ActionEvent e) {
	        Person newPerson = new Person();
	        PersonPanel.setModel(newPerson);
	        listModel.addElement(newPerson);
	        PersonList.setSelectedIndex(listModel.getSize() - 1);
        }
    }

    private class RemovePersonListener implements ActionListener {

        @Override
        public void actionPerformed(ActionEvent e) {
	        if (!PersonList.isSelectionEmpty()) {
		        PersonPanel.setModel(null);
		        PersonPanel.clearAll();
		        listModel.remove(PersonList.getSelectedIndex());
	        }
        }
    }

	public static void main(String[] args) {
        JFrame frame = new JFrame("Øving T4");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        PersonListPanel p = new PersonListPanel();

        Person p1 = new Person("Håkon");
        Person p2 = new Person("Truls");
        Person p3 = new Person("Fredrik");
	    Person p4 = new Person("Lars");
	    Person p5 = new Person("Kradalby");
	    Person p6 = new Person("Steffen");

        DefaultListModel<Person> m = new DefaultListModel<Person>();
        m.addElement(p1);
        m.addElement(p2);
        m.addElement(p3);
	    m.addElement(p4);
	    m.addElement(p5);
	    m.addElement(p6);

        p.setModel(m);

        frame.setContentPane(p);
        frame.pack();
        frame.setVisible(true);
    }
}

