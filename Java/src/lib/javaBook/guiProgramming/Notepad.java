package lib.javaBook.guiProgramming;

import java.awt.*;
import java.awt.event.*;
import java.awt.event.KeyEvent;
import javax.swing.*;
import javax.swing.JOptionPane;
import java.io.*;
import java.util.*;
import javax.swing.event.*;

public class Notepad extends JFrame implements ActionListener {
	JLabel statusBar;
	JFrame f1 = new JFrame("Editor");
	JTextArea ta;
	JMenuBar mb;
	JMenu file, edit, view, format, help;
	JMenuItem new1, open, save, close, cut, copy, paste, print, status, wordwrap, font, viewhelp, aboutnotepad;
	JFileChooser fc;
	Scanner s = null;
	Font fa;
	JScrollPane jsp;
	JLabel l1;
	ImageIcon i1;
	JFrame f2;
	JFrame f3;
	JButton b1, bb1;
	JButton b2, bb2;

	JComboBox c1;
	JComboBox c2;
	JComboBox c3;

	JPanel p1 = new JPanel();

	public Notepad() {
// Create frame in java
		f1 = new JFrame();

// Java Jframe set title
		f1.setTitle("Tahsin IDE");

// Jframe set size in java
		f1.setSize(900, 900);

// add Set Visible to display frame
		f1.setVisible(true);

// Complete clode the program
		f1.setDefaultCloseOperation(EXIT_ON_CLOSE);

		f2 = new JFrame("about notepad");
		f3 = new JFrame("format");
//statusBar=new JLabel();
		statusBar = new JLabel("|| Ln 1, Col 1  ", JLabel.RIGHT);
// Add element in combobox 
		String sj2[] = { "Arial", "TimesRoman", "Cooper", "Consolas" };
		c1 = new JComboBox(sj2);
		String sj1[] = { "BOLD", "ITALIC" };
		c2 = new JComboBox(sj1);
// Text Size 
		String sj[] = { "100", "95", "90", "85", "80", "75", "70", "65", "60", "55", "50", "45", "40", "35", "45", "25",
				"40", "30", "16", "17", "18", "19", "15", "14", "13", "12", "11", "10", "9", "8", "7" };
		c3 = new JComboBox(sj);
// Creade button
		bb1 = new JButton("ok");
		bb2 = new JButton("cancel");
		f3.setSize(300, 300);
		f3.setLayout(new FlowLayout());
// Perform ActionListener on Buttons
		bb2.addActionListener(this);
		bb1.addActionListener(this);
		// Set front style and Size
		fa = new Font("Arial", Font.BOLD, 45);
		fc = new JFileChooser();
		// Set Jtextarea
		ta = new JTextArea(60, 60);
		ta.setFont(fa);
		ta.setBounds(0, 20, 800, 500);
// Set the location of Menu bar
		mb = new JMenuBar();
		mb.setBounds(0, 0, 800, 30);
// Add element in menu
//mb.add(file);
//file.add(open);
		file = new JMenu("File");
		edit = new JMenu("Edit");
		view = new JMenu("view");
		format = new JMenu("format");
		help = new JMenu("Help");
		// Create menu
		new1 = new JMenuItem("new");
		open = new JMenuItem("open");
		save = new JMenuItem("save");
		close = new JMenuItem("close");
		print = new JMenuItem("print");
		cut = new JMenuItem("cut");
		copy = new JMenuItem("copy");
		paste = new JMenuItem("paste");
		// Set Jmenu Item
		status = new JMenuItem("status bar");
		viewhelp = new JMenuItem("ViewHelp");
		aboutnotepad = new JMenuItem("about notepad");
		font = new JMenuItem("font");
		wordwrap = new JMenuItem("word wrap");
		// Add ImageIcon in java example
		i1 = new ImageIcon("notepad.png");
		l1 = new JLabel(i1);
		f2.add(l1);
		// Add menu inside the menu bar
		mb.add(file);
		mb.add(edit);
		mb.add(format);
		mb.add(help);
		mb.add(view);
		p1.add(mb, BorderLayout.NORTH);
		p1.setLayout(new BorderLayout());
		// add menu inside the file menu
		file.add(new1);
		file.addSeparator();
		file.add(open);
		file.addSeparator();
		file.add(save);
		file.addSeparator();
		file.add(close);
		file.addSeparator();
		file.add(print);
		file.addSeparator();
		// add menu inside the edit menu
		edit.add(cut);
		file.addSeparator();

		edit.add(copy);
		file.addSeparator();

		edit.add(paste);
		file.addSeparator();

		view.add(status);

		format.add(wordwrap);
		file.addSeparator();

		format.add(font);
		file.addSeparator();
		help.add(viewhelp);
		file.addSeparator();
		help.add(aboutnotepad);
		f3.add(c1);
		f3.add(c2);
		f3.add(c3);
		f3.add(bb1);
		f3.add(bb2);
		view.addSeparator();
		file.setMnemonic(KeyEvent.VK_F);
		edit.setMnemonic(KeyEvent.VK_E);
		view.setMnemonic(KeyEvent.VK_Y);
		KeyStroke opn = KeyStroke.getKeyStroke(KeyEvent.VK_O, KeyEvent.CTRL_DOWN_MASK);
		open.setAccelerator(opn);

		KeyStroke n1 = KeyStroke.getKeyStroke(KeyEvent.VK_N, KeyEvent.CTRL_DOWN_MASK);
		new1.setAccelerator(n1);

		KeyStroke sav = KeyStroke.getKeyStroke(KeyEvent.VK_S, KeyEvent.CTRL_DOWN_MASK);
		save.setAccelerator(sav);

		KeyStroke clos = KeyStroke.getKeyStroke(KeyEvent.VK_L, KeyEvent.CTRL_DOWN_MASK);
		close.setAccelerator(clos);

		KeyStroke prnt = KeyStroke.getKeyStroke(KeyEvent.VK_P, KeyEvent.CTRL_DOWN_MASK);
		print.setAccelerator(prnt);

		KeyStroke cu = KeyStroke.getKeyStroke(KeyEvent.VK_X, KeyEvent.CTRL_DOWN_MASK);
		cut.setAccelerator(cu);

		KeyStroke cpy = KeyStroke.getKeyStroke(KeyEvent.VK_C, KeyEvent.CTRL_DOWN_MASK);
		copy.setAccelerator(cpy);

		KeyStroke pst = KeyStroke.getKeyStroke(KeyEvent.VK_V, KeyEvent.CTRL_DOWN_MASK);
		paste.setAccelerator(pst);

		KeyStroke ab = KeyStroke.getKeyStroke(KeyEvent.VK_B, KeyEvent.CTRL_DOWN_MASK);
		status.setAccelerator(ab);
		// add action listener on menu element
		new1.addActionListener(this);
		open.addActionListener(this);
		save.addActionListener(this);
		close.addActionListener(this);
		cut.addActionListener(this);
		copy.addActionListener(this);
		paste.addActionListener(this);
		print.addActionListener(this);
		viewhelp.addActionListener(this);
		aboutnotepad.addActionListener(this);
		wordwrap.addActionListener(this);
		font.addActionListener(this);
		status.addActionListener(this);
		JScrollPane js = new JScrollPane(ta);
		js.setHorizontalScrollBarPolicy(JScrollPane.HORIZONTAL_SCROLLBAR_ALWAYS);
		js.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_ALWAYS);
		/*
		 * JScrollPane.VERTICAL_SCROLLBAR_ALWAYS,JScrollPane.
		 * HORIZONTAL_SCROLLBAR_AS_NEEDED);
		 */
		p1.add(js, BorderLayout.CENTER);
		p1.add(mb, BorderLayout.NORTH);
		p1.add(statusBar, BorderLayout.SOUTH);
		f1.add(p1);

		addWindowListener(new WindowAdapter() {

			public void windowClosing(WindowEvent we) {
				int n;
// Display dialogbox

				n = JOptionPane.showOptionDialog(null, "Do you want tosave your changees?", "Notepad",
						JOptionPane.YES_NO_OPTION, JOptionPane.QUESTION_MESSAGE, null, null, null);

				if (n == JOptionPane.NO_OPTION) {
					System.exit(0);
				} else if (n == JOptionPane.CLOSED_OPTION) {
					f1.setVisible(true);
				} else if (n == JOptionPane.YES_OPTION) {
					System.out.println("hai");
					JFrame i = new JFrame();
					int p = fc.showSaveDialog(i);
					if (p == JFileChooser.APPROVE_OPTION) {
						try {
							FileWriter f1 = new FileWriter(fc.getSelectedFile());
							BufferedWriter br = new BufferedWriter(f1);
							s = new Scanner(ta.getText());
							while (s.hasNext()) {
								br.write(s.nextLine());
								br.newLine();
							}
							br.close();
						}

						catch (IOException ie) {
							System.out.println(ie);
						}
					}
				}
				System.exit(0);
			}
		});

		ta.addCaretListener(new CaretListener() {
			public void caretUpdate(CaretEvent e) {
				int lineNumber = 0, column = 0, pos = 0;
				try {
					pos = ta.getCaretPosition();
					lineNumber = ta.getLineOfOffset(pos);
					column = pos - ta.getLineStartOffset(lineNumber);
				} catch (Exception excp) {
				}
				if (ta.getText().length() == 0) {
					lineNumber = 0;
					column = 0;
				}
				statusBar.setText("||Ln " + (lineNumber + 1) + ", Col " + (column + 1));
			}
		});
	}

// Action Performed Java GUI notepad editor project
	public void actionPerformed(ActionEvent ae) {
		if (ae.getSource().equals(new1)) {
			ta.setText("");
		}
		if (ae.getSource().equals(close)) {
			System.exit(0);
		}
		if (ae.getSource().equals(open)) {
			ta.setText("");
			int n = fc.showOpenDialog(this);
			if (n == JFileChooser.APPROVE_OPTION) {
				try {
					Scanner sc = new Scanner(fc.getSelectedFile());
					while (sc.hasNext()) {
						String str = sc.nextLine();
						ta.append(str + "n");
					}
				} catch (FileNotFoundException aie) {
					System.out.println(aie);
				}
			}
		}

		if (ae.getSource().equals(save)) {
			int p = fc.showSaveDialog(this);
			if (p == JFileChooser.APPROVE_OPTION) {
				try {
					FileWriter f1 = new FileWriter(fc.getSelectedFile());
					File select = fc.getSelectedFile();
					if (select.exists())
						JOptionPane.showMessageDialog(null, "file already exists,enter another filename");
					else {

						BufferedWriter br = new BufferedWriter(f1);
						s = new Scanner(ta.getText());
						while (s.hasNext()) {
							br.write(s.nextLine());
							br.newLine();
						}
						br.close();

					}
				} catch (IOException ex) {
					System.out.println(ex);
				}
			}
		}

		if (ae.getSource().equals(cut)) {
			ta.cut();
		}
		if (ae.getSource().equals(status)) {
			/*
			 * ta.addCaretListener( new CaretListener() { public void
			 * createUpdate(CaretEvent e) { int ln=0,clm=0,pos=0; try {
			 * pos=ta.getCaretPosition(); ln=ta.getLineOfOffset(pos);
			 * clm=pos-ta.getLineStartOffset(ln); }catch(Exception excp){}
			 * if(ta.getText().length()==0) { ln=0; clm=0; }
			 * statusBar.setText("|| ln"+(ln+1)+" col"+(clm+1)); } });
			 */

		}

		if (ae.getSource().equals(copy)) {
			/*
			 * Font f2=new Font("Arial",Font.ITALIC,18); ta.setFont(f2);
			 */
			ta.copy();
		}
		if (ae.getSource().equals(paste)) {
			ta.paste();
		}
		if (ae.getSource().equals(print)) {
			try {
				ta.print();
			} catch (Exception pe) {
				System.out.print(pe);
			}
		}
		if (ae.getSource().equals(viewhelp)) {// System.out.println("hai go to browser");
			JOptionPane.showMessageDialog(null, "go and search in browser");
		}
		if (ae.getSource().equals(aboutnotepad)) {
			f2.setVisible(true);

		}
		if (ae.getSource().equals(font)) {
			f3.setVisible(true);
		}
		if (ae.getSource().equals(bb1)) {
			String lo = (String) c1.getSelectedItem();
			String lo1 = (String) c2.getSelectedItem();
			int i1 = Integer.parseInt((String) c3.getSelectedItem());
			Font fff = new Font("Cooper", Font.BOLD, 10);
			if (lo1.equals("BOLD")) {
				fff = new Font(lo, Font.BOLD, i1);
			}
			if (lo1.equals("ITALIC")) {
				fff = new Font(lo, Font.ITALIC, i1);
			}
			ta.setFont(fff);
			JOptionPane.showMessageDialog(null, "font changed");
			f3.setVisible(false);
		}
		if (ae.getSource().equals(bb2))
			f3.setVisible(false);
	}

	public static void main(String args[]) {
		new Notepad();
	}
}

// package lib.javaBook.guiProgramming;

// import java.awt.event.ActionListener;
// import java.io.BufferedReader;
// import java.io.IOException;
// import java.io.InputStreamReader;
// import java.awt.Color;
// import java.awt.Cursor;
// import java.awt.Font;
// import java.awt.event.ActionEvent;
// import javax.swing.JButton;
// import javax.swing.JFrame;
// import javax.swing.JScrollPane;
// import javax.swing.JTextArea;
// import javax.swing.JTextField;

// public class Editor {
// 	public Editor() {
// 		JFrame jfrm = new JFrame("Editor.exe");
// 		jfrm.setVisible(true);
// 		jfrm.setSize(1090, 1080);
// 		jfrm.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
// 		jfrm.setLayout(null);

// 		JButton button = new JButton("Compile and Run");
// 		button.setBounds(20, 20, 300, 50);

// 		button.addActionListener(new ActionListener() {

// 			public void actionPerformed(ActionEvent e) {
//                 ProcessBuilder processBuilder = new ProcessBuilder();

// 				processBuilder.command("cmd.exe", "/c", "start \"\" E:\\test.bat");

// 				try {

// 					Process process = processBuilder.start();

// 					StringBuilder output = new StringBuilder();

// 					BufferedReader reader = new BufferedReader(
// 							new InputStreamReader(process.getInputStream()));

// 					String line;
// 					while ((line = reader.readLine()) != null) {
// 						output.append(line + "\n");
// 					}

// 					int exitVal = process.waitFor();
// 					if (exitVal == 0) {
// 						System.out.println(output);
// 					} else {

// 					}
// 					} catch (IOException l) {
// 						l.printStackTrace();
// 					} catch (InterruptedException i) {
// 						i.printStackTrace();
// 					}
//         		}

//     		}); 

// 		Font font = new Font("Consolas", Font.PLAIN , 25);
// 		JTextArea jText = new JTextArea();
// 		jText.setLineWrap(true);
// 		JScrollPane scroll = new JScrollPane (jText);
// 		scroll.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_ALWAYS);
//      scroll.setHorizontalScrollBarPolicy(JScrollPane.HORIZONTAL_SCROLLBAR_ALWAYS);

// 		jText.setBounds(5, 70, 400000, 1090000);
// 		jText.setFont(font);

// 		jfrm.add(button);
// 		jfrm.add(jText);
// 		jfrm.add(scroll);
// 	}
// }
