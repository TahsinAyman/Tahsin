package lib.multithred;


public class MultiThread implements Runnable {
    private int start;
    private int to;
    private int much;

    public MultiThread(int start, int to, int much) {
        this.start = start;
        this.to = to;
        this.much = much;
    }

    public MultiThread(int start, int to) {
        this.start = start;
        this.to = to;
        this.much = 1;
    }

    public MultiThread(int to) {
        this.start = 1;
        this.to = to;
        this.much = 1;
    }

    public int getStart() {
        return start;
    }

    public void setStart(int start) {
        this.start = start;
    }

    public int getTo() {
        return to;
    }

    @Override
    public String toString() {
        return "MultiThread{" +
                "start=" + start +
                ", to=" + to +
                ", much=" + much +
                '}';
    }

    public void setTo(int to) {
        this.to = to;
    }

    public int getMuch() {
        return much;
    }

    public void setMuch(int much) {
        this.much = much;
    }

    @Override
    public void run() {
        for (int i = this.start; i <= this.to; i = i + this.much) {
            System.out.println(i);
            try {
                Thread.sleep(100);
            } catch (InterruptedException ie) {

            }


        }
    }

}
