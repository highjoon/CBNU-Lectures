package public_void;

import private_this.CarC;

public class CarDtest {

	public static void main(String[] args) {
		
		CarD myCar1 = new CarD();
		myCar1.setColor("����");
		myCar1.setSpeed(0);
		
		myCar1.upSpeed(30);
		
		System.out.println("�ڵ��� 1�� ������ " + myCar1.getColor() + "�̸�, ���� �ӵ��� " + myCar1.getSpeed() + "km �Դϴ�.");


	}

}
