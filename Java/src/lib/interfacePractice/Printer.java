package lib.interfacePractice;

public class Printer implements Printable {
    private String text;

    public Printer(String text) {
        this.text = text;
    }

    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public void print() {
        System.out.println(this.text);
    }
}
