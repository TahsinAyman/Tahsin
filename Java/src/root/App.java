package root;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class App {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Button");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 450);
        frame.setVisible(true);
        frame.setLayout(new FlowLayout());

        JButton button = new JButton();
        button.setBounds(50, 50, 300, 300);
        frame.add(button);
    }
}
