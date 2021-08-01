package edu.cbnu.CarTest7;

public class Car {
	
	int speed = 0;
	
	final void upSpeed(int speed) {
		this.speed += speed;
	}
}

class Sedan extends Car {
	final static String CAR_TYPE = "½Â¿ëÂ÷";
}