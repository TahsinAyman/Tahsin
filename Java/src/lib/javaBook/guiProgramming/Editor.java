package lib.javaBook.guiProgramming;

import java.awt.event.ActionListener;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import static javax.swing.ScrollPaneConstants.HORIZONTAL_SCROLLBAR_ALWAYS;
import java.awt.Color;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.io.EOFException;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import static javax.swing.ScrollPaneConstants.HORIZONTAL_SCROLLBAR_ALWAYS;
import java.awt.Color;
import java.awt.Font;
import java.awt.event.ActionEvent;

import javax.swing.Action;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;

public class Editor {
	public Editor() {

		JFrame jfrm = new JFrame("Editor.exe");
		jfrm.setVisible(true);
		jfrm.setSize(1090, 1080);
		jfrm.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		jfrm.setLayout(null);


		JButton button = new JButton("Compile and Run");
		button.setBounds(20, 20, 300, 50);

		button.addActionListener(new ActionListener() {

			public void actionPerformed(ActionEvent e) {
				ProcessBuilder processBuilder = new ProcessBuilder();

				processBuilder.command("E:\\run.bat");

				try {

					Process process = processBuilder.start();

					StringBuilder output = new StringBuilder();

					BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
					String line;
					while ((line = reader.readLine()) != null) {
						output.append(line + "\n");
					}

					int exitVal = process.waitFor();
					if (exitVal == 0) {
						System.out.println(output);
					} else {

					}
					} catch (IOException l) {
						l.printStackTrace();
					} catch (InterruptedException i) {
						i.printStackTrace();
					}
        		}

    		}); 

		Font font = new Font("Consolas", Font.PLAIN , 25);
		JTextArea jText = new JTextArea();
		jText.setLineWrap(true);
		JScrollPane scroll = new JScrollPane (jText);
        scroll.setHorizontalScrollBarPolicy(HORIZONTAL_SCROLLBAR_ALWAYS);
		scroll.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_ALWAYS);

		jText.setBounds(5, 70, 400000, 1090000);
		jText.setFont(font);

		jfrm.add(button);
		jfrm.add(jText);
		jfrm.getContentPane ().add(scroll);
	
		JButton loadButton = new JButton("Load");
		loadButton.setBounds(500, 20, 100, 50);

		loadButton.addActionListener(new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent e) {
				String text = "";
				try {
					FileReader fr = new FileReader("E:\\App.c");
					int i;
					while ((i = fr.read()) != -1)
						text += (char) i;
					fr.close();
				} catch (IOException ex) {
					System.out.println(ex);
				}
				jText.setText(text);
			}
		});

		JButton button2 = new JButton("Save");
		button2.setBounds(350, 20, 100, 50);

		button2.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				try {
					FileWriter fw = new FileWriter("E:\\App.c");
					fw.write(jText.getText());
					fw.close();
				} catch (Exception f) {
					System.out.println(f);
				}
			}
		});

		jfrm.add(button);
		jfrm.add(button2);
		jfrm.add(loadButton);
		jfrm.add(jText);
		jfrm.getContentPane().add(scroll);
	}
}
