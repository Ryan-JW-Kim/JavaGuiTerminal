import javax.swing.*;
import java.awt.event.*;
import java.awt.*;
import java.io.*;
import java.time.LocalTime;

public class Alarm {

	static JPanel panel = new JPanel();
	static JButton alarmBtn = new JButton("Start Alarm");


	public void compile() { 

		alarmBtn.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {

				try {

					ProcessBuilder pb = new ProcessBuilder("python3","test.py");
					Process p = pb.start();

					int exitNum = p.waitFor();

					BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));

					String ret = in.readLine();

					System.out.println(LocalTime.now());
					}

				catch (Exception er) { System.out.println(er); }
				}
			});
		
		panel.add(alarmBtn);
		}
	}