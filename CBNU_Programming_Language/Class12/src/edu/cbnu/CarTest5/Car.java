package edu.cbnu.CarTest5;

public class Car {
	protected String color;
	int speed;
}

class Sedan extends Car {
	void setSpeed(int speed) {
		this.speed = speed;
	}
	
	void setColor(String color) {
		this.color = color;
	}
}
