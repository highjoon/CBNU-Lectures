package edu.cbnu.CarTest9;

abstract class Car {
	int speed = 0;
	String color;
	
	void upSpeed(int speed) {
		this.speed += speed;
	}
	
	abstract void work();  // work() �޼ҵ带 �߻� �޼ҵ�� ����. �� �߻� �޼ҵ�� ���� Car Ŭ������ �ݵ�� �߻� Ŭ������ ����. 
}

class Sedan extends Car {
	void work() {																			    // ����Ŭ�������� �߻� �޼ҵ带 �ݵ�� �������̵� �ؾ���.
		System.out.println("�¿����� ����� �¿�� �ֽ��ϴ�.");  // ����Ŭ������ �ʿ��� ������ ä��.
	}
}

class Truck extends Car {
	void work() {																				// ����Ŭ�������� �߻� �޼ҵ带 �ݵ�� �������̵� �ؾ���.
		System.out.println("Ʈ���� ���� �ư� �ֽ��ϴ�.");				// ����Ŭ������ �ʿ��� ������ ä��.
	}
}