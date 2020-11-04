package public_void;

public class CarD {
	
	private String color;
	private int speed;
	
	public void upSpeed(int value) {
		speed += value;
	}
	
	public void downSpeed(int value) {
		speed -= value;
	}
	
	public String getColor() {
		return color;
	}
	
	public int getSpeed() {
		return speed;
	}
	
	public void setColor(String color) {
		this.color = color;
	}
	
	public void setSpeed(int speed) {
		this.speed = speed;
	}
}
