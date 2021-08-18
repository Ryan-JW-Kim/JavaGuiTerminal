import javax.swing.*;
import java.awt.event.*;
import java.awt.*;
import java.io.*;
import java.time.LocalTime;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class Alarm {

	static JPanel panel = new JPanel();
	static JButton alarmBtn = new JButton("Start Alarm");

	public static void log(String logLine) {

		try {

			File file = new File("log.txt");
			FileWriter myWriter = new FileWriter("log.txt", true);

			myWriter.write(logLine + "\n");
			myWriter.close();
			System.out.println("Successfully loged");
			}

		catch (IOException e) {

			System.out.println("Error occured while writing");
			e.printStackTrace();
			}

		}

	public void compile() { 

		alarmBtn.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {

				try {

					ProcessBuilder pb = new ProcessBuilder("python3","test_sys.py");
					Process p = pb.start();

					int exitNum = p.waitFor();

					BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));

					String ret = in.readLine();

					log(ret);
					System.out.println("Logged --> " + ret);

					}

				catch (Exception er) { System.out.println(er); }
				}
			});
		
		panel.add(alarmBtn);
		}
	}
