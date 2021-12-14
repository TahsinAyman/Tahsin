package lib.io.filehandaling;

import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class FileInput {
    public FileInput() {
        String text;
        Scanner input = new Scanner(System.in);
        text = input.next();
        try {
            FileWriter fwrite = new FileWriter("file.txt");
            fwrite.write(text);
            fwrite.close();
        } catch (IOException e) {
            System.out.println("Error!");
        }
    }
}
