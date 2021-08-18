import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

class Main extends JFrame {

	static JFrame frame = new JFrame("Window Title");

	Main() { }

	public static void main(String[] args) {

		Home homePanel = new Home();
		homePanel.compile();

		frame.add(homePanel.panel);
		//Alarm alarmPanel = new Alarm();

		homePanel.addBtn.addActionListener(new ActionListener() {

			public void actionPerformed(ActionEvent e) {

				System.out.println("Pressed");

				frame.getContentPane().removeAll();
				frame.repaint();

				//frame.remove(homePanel.panel);
				
				Alarm alarmPanel = new Alarm();
				alarmPanel.compile();

				frame.add(alarmPanel.panel);

				}
			});


		//frame.add(alarmPanel.panel);

		frame.setSize(300,400);

		frame.setVisible(true);

		}
	}