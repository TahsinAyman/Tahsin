package lib.vehicle;

import java.io.IOException;

public class Vehicle {
    private int speed;
    private int toSpeed;
    private int wheelThiknessCM;
    private String name;

    
    
    public Vehicle() {

	}
	public Vehicle(String name) {
		this.name = name;
	}
	public Vehicle(int speed, String name) {
		super();
		this.speed = speed;
		this.name = name;
	}
	public void setName(String name) {
        this.name = name;
    }
    public String getName() {
        return name;
    }
    public void setWheelThiknessCM(int wheelThiknessCM) {
        this.wheelThiknessCM = wheelThiknessCM;
    }
    public int getWheelThiknessCM() {
        return wheelThiknessCM;
    }
    public void setToSpeed(int toSpeed) {
        this.toSpeed = toSpeed;
    }
    public int getToSpeed() {
        return toSpeed;
    }
    public void run() {
        for (int i = 1; i <= toSpeed; i++) {
            speed++;
        }
    }
    public void stop() {
        speed = 0;
    }

    @Override
    public String toString() {
        return  "Vehicle Name: " + name + "\nWheel Thikness: " + wheelThiknessCM + " Centimiter\n";
    }
    public String afterRunningSpeed() {
        return "After Running Speed: "  + speed + "\n";
    }
    public String afterStoppingSpeed() {
        return "After Stopping Speed: " + speed + "\n";
    }
    public void printFileContent() throws IOException{
    	System.out.println("im here");
    	throw new IOException();
    }
    
}