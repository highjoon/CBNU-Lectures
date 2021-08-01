package edu.cbnu.CarTest9;

abstract class Car {
	int speed = 0;
	String color;
	
	void upSpeed(int speed) {
		this.speed += speed;
	}
	
	abstract void work();  // work() 메소드를 추상 메소드로 지정. 이 추상 메소드로 인해 Car 클래스는 반드시 추상 클래스로 지정. 
}

class Sedan extends Car {
	void work() {																			    // 서브클래스에서 추상 메소드를 반드시 오버라이딩 해야함.
		System.out.println("승용차가 사람을 태우고 있습니다.");  // 서브클래스에 필요한 내용을 채움.
	}
}

class Truck extends Car {
	void work() {																				// 서브클래스에서 추상 메소드를 반드시 오버라이딩 해야함.
		System.out.println("트럭이 짐을 싣고 있습니다.");				// 서브클래스에 필요한 내용을 채움.
	}
}