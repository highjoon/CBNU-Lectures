package edu.cbnu.CarTest6;

class Car {
	int speed = 0;
	
	void upSpeed(int speed) {
		this.speed += speed;
		System.out.println("현재 속도 (슈퍼클래스) : " + this.speed);
	}
}

	class Sedan extends Car {
		void upSpeed(int speed) {
		this.speed += speed;
		if (this.speed > 150) {
			this.speed  = 150;
		} System.out.println("현재 속도 (서브클래스) : " + this.speed);
	}
}

	class Truck extends Car {
	}