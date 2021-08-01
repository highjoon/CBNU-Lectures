package edu.cbnu.CarTest2;

public class Car {
	Car() {
		System.out.println("슈퍼 클래스 생성자 호출");
	}
}

class Sedan extends Car {
	Sedan() {
		System.out.println("서브 클래스 생성자 호출");
	}
}