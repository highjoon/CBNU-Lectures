package private_this;

public class CarC {
	
	private String color;
	private int speed;
	
	void upSpeed(int value) {
		speed += value;
	}
	
	void downSpeed(int value) {
		speed -= value;
	}
	
	String getColor() {
		return color;
	}
	
	int getSpeed() {
		return speed;
	}
	
	void setColor(String color) {
		this.color = color;
	}
	
	void setSpeed(int speed) {
		this.speed = speed;
	}
}
