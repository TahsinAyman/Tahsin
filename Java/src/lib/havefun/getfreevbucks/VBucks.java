package lib.havefun.getfreevbucks;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class VBucks {
    public VBucks() {    
        JFrame frame = new JFrame("Get VBucks in Authentic way!!!");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(1090, 1080);
        frame.setVisible(true);
        frame.setLayout(null);
        
        JButton button = new JButton("Click here to get VBucks");
        button.setBounds(50, 50, 200, 50);

        button.addActionListener((ActionListener) new ActionListener() {
            
            public void actionPerformed(ActionEvent e) {

                int cardNumber = Integer.parseInt(JOptionPane.showInputDialog("Enter your Credit card Number"));

                JOptionPane optionPane = new JOptionPane();
                optionPane.showMessageDialog(null, "Notification: Thanks for Purchasing");
                optionPane.showMessageDialog(null, "Download FreeVBucks.exe");
                optionPane.showMessageDialog(null, "Notification: Your Device has been infected by RansomWare Virus");
                optionPane.showMessageDialog(null, "Notification: Your Credit card has been Hacked");
                optionPane.showMessageDialog(null, "Notification: Thanks for Sending 10,000 $");
                optionPane.showMessageDialog(null, "You got Trolled");
                optionPane.showMessageDialog(null, "You: What!!!");
                System.exit(0);
            }
        
        });

        frame.add(button);
    }
}
