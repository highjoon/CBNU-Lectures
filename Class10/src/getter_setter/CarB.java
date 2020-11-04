package getter_setter;

public class CarB {
	
	String color;
	int speed;
	
	void upSpeed(int value) {
		speed += value;
	}
	
	void downSpeed(int value) {
		speed -= value;
	}

	public String getColor() {
		return color;
	}

	public int getSpeed() {
		return speed;
	}
	
	
}
