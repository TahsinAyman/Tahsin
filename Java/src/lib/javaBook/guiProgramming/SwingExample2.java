package lib.javaBook.guiProgramming;

import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.border.Border;

public class SwingExample2 {
	
	private String name = null;
	private int age = 0;

	public SwingExample2() {
    	
        JFrame jFrame = new JFrame("Tahsin");
        jFrame.setVisible(true);
        jFrame.setSize(1920, 1080);
        jFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        jFrame.setLayout(null);

        JPanel panel = new JPanel();
        panel.setBounds(5, 5, 100, 550);
        panel.setLayout(null);
        
        Border border = BorderFactory.createLineBorder(Color.BLACK, 1);

        JLabel jName = new JLabel("Your Name: "+ this.name+ JLabel.CENTER);
        jName.setBounds(5, 75, 150, 20);
        jName.setBorder(border);
        
        JLabel jAge = new JLabel("Your Age: " + this.age);
        jAge.setBounds(5, 100, 150, 20);
        jAge.setBorder(border);
        
        JTextField jNameTxt = new JTextField("Enter Name");
        jNameTxt.setBounds(160, 75, 200, 20);
        
        JTextField jAgeTxt = new JTextField("Enter Age");
        jAgeTxt.setBounds(160, 102, 200, 20);
        
        jNameTxt.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				jName.setText(jNameTxt.getText());
			}
		});
        
        jAgeTxt.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				jAge.setText(jAgeTxt.getText());
			}
		});
        
        
        JLabel jText = new JLabel("Home");
        jText.setForeground(Color.BLACK);
        jText.setBounds(750, 3, 200, 20);

        JOptionPane jOptionPane = new JOptionPane();
        
        JButton button2 = new JButton("Register");
        button2.setBackground(Color.gray);
        button2.setBounds(5, 20, 100, 50);

        button2.addActionListener(new ActionListener() {

                public void actionPerformed(ActionEvent e) {
        		
                    jName.setText(jOptionPane.showInputDialog("Enter your Name"));
        		    jAge.setText((jOptionPane.showInputDialog("Enter your Age")));
        		
        	}
        	
        });
        
        JButton button = new JButton("Exit");
        button.setLayout(null);
        button.setBackground(Color.BLACK);
        button.setText("Exit");
        button.setForeground(Color.WHITE);
        button.setBounds(500, 780, 500, 20);
        button.addActionListener(new ActionListener() {

			public void actionPerformed(ActionEvent e) {
                System.exit(0);
            }
        	

        });
        
        JButton button3 = new JButton();
        button3.setText("Information");
        button3.setBackground(Color.BLACK);
        button3.setForeground(Color.WHITE);
        button3.setBounds(1050, 780, 200, 400); 

        jFrame.add(button3);
        jFrame.add(button);
        jFrame.add(button2);
        jFrame.add(jText);
        jFrame.add(jOptionPane);
        jFrame.add(jName);
        jFrame.add(jAge);
        jFrame.add(jNameTxt);
        jFrame.add(jAgeTxt);
    }
}
