package edu.cbnu.CarTest8;

abstract class Car {
	int speed = 0;
	String color;
	
	void upSpeed(int speed) {
		this.speed += speed;
	}
}

class Sedan extends Car {}

class Truck extends Car {}