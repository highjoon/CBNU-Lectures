package edu.cbnu.CarTest3;

public class Car {
	Car() {
		System.out.println("���� Ŭ���� ������ ȣ�� (�Ķ���� ����)");
	}
	
	Car(String str) {
		System.out.println("���� Ŭ���� ������ ȣ�� ==> " + str);
	}
}

class Sedan extends Car {
	Sedan(String str) {
		
		super(str);
		
		System.out.println("���� Ŭ���� ������ ȣ�� ==> " + str);
	}
}