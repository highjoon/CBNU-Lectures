package private_public;

public class CarE {
	private int speed = 0;
	
	public void upSpeed(int value) {
		if (speed + value > 200) {
			speed = 200;
		} else {
			speed += value;
		}
		
		System.out.println("���� �ӵ� ==> " + getSpeed());
	}
	
	public void downSpeed(int value) {
		if (speed - value < 0) {
			speed = 0;
		} else {
			speed -= value;
		}
		
		System.out.println("���� �ӵ� ==> " + getSpeed());
	}
	
	public int getSpeed() {
		return speed;
	}
}
