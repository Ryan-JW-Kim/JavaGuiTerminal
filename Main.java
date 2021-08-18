import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

class Main extends JFrame {

	static JFrame frame = new JFrame("Window Title");

	Main() { }

	public static void newPanel(JFrame myFrame, JPanel panel) {

		myFrame.getContentPane().removeAll();
		myFrame.repaint();

		myFrame.add(panel);

		myFrame.revalidate();

		}

	public static void main(String[] args) {

		// Making components of the Home Panel

		JPanel homePanel = new JPanel();
		JButton AlarmBtn = new JButton("Alarm");

		// Defining button actions to navigate to other panels

		AlarmBtn.addActionListener(new ActionListener() {

			public void actionPerformed(ActionEvent e) {

				Alarm alarmPanel = new Alarm();
				alarmPanel.compile();

				newPanel(frame, alarmPanel.panel);
				}
			});

		// Adding Home Panel components to the main frame

		frame.add(homePanel);
		frame.add(AlarmBtn);

		// Frame layout
		frame.setSize(300,400);
		frame.setLayout(new FlowLayout());
		frame.setVisible(true);

		}
	}
