package oving4;

import javax.imageio.ImageIO;
import javax.swing.*;
import java.awt.*;

/**
 * Created by hakloev on 23/01/14.
 */
public class PersonRenderer extends DefaultListCellRenderer implements ListCellRenderer<Object> {

	ImageIcon male = new ImageIcon(getClass().getResource("male.png"));
	ImageIcon female = new ImageIcon(getClass().getResource("female.png"));

	@Override
	public Component getListCellRendererComponent(JList list, Object value, int index, boolean isSelected, boolean cellHasFocus) {

		JLabel label = (JLabel) super.getListCellRendererComponent(list, value, index, isSelected, cellHasFocus);

		Person p = (Person) value;
		String text = new String();
		if (p.getName() == null) {
			text += "No name";
		} else {
			text += p.getName();
		}
		if (p.getEmail() == null) {
			text += " # No email";
		} else {
			text += " # " + p.getEmail();
		}

		label.setText(text);
		if (isSelected) {
			label.setBackground(Color.GRAY);
		}

		if (p.getGender() != null) {
			if (p.getGender() == Gender.male) {
				Image img = male.getImage();
				Image newImg = img.getScaledInstance(15, 15, Image.SCALE_SMOOTH);
				label.setIcon(new ImageIcon(newImg));
			} else {
				Image img = female.getImage();
				Image newImg = img.getScaledInstance(15, 15, Image.SCALE_SMOOTH);
				label.setIcon(new ImageIcon(newImg));
			}
		} else {
			//TODO

		}

		return label;
	}

}
