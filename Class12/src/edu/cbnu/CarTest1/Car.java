package edu.cbnu.CarTest1;

public class Car {
	String color;
	int speed;
	
	void upSpeed(int value) {
		speed += value;
	}
	
	void downSpeed(int value) {
		speed -= value;
	}
}

class Sedan extends Car {
	int seatNum;
	
	int getSeatNum() {
		return seatNum;
	}
}

class Truck extends Car {
	int capacity;
	
	int getCapacity() {
		return capacity;
	}
}