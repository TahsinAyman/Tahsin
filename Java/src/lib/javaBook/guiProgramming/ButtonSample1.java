package lib.javaBook.guiProgramming;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class ButtonSample1 implements ActionListener {
    public ButtonSample1() {
        JFrame frame = new JFrame("Button");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 450);
        frame.setVisible(true);
        frame.setLayout(new FlowLayout());

        JButton button = new JButton();
        button.setBounds(50, 50, 300, 300);
        button.addActionListener(this);
        frame.add(button);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        // TODO Auto-generated method stub
        
    }
}
