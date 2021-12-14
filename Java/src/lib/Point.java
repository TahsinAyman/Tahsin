package lib;

public class Point {
    private int x;
    private int y;

    public Point(int xValue , int yValue) {
        x = xValue;
        x = yValue;
    }
    public void setX(int xValue) {
        this.x = xValue;
    }
    public int getX() {
        return x;
    }
    public void setY(int yValue) {
        this.y = yValue;
    }
    public int getY() {
        return y;
    }

    @Override
    public String toString() {
        return "Point [x=" + x + ", y=" + y + "]";
    }

    
}
