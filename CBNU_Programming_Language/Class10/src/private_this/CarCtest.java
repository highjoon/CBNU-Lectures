package private_this;

public class CarCtest {

	public static void main(String[] args) {
		
		CarC myCar1 = new CarC();
		myCar1.setColor("����");
		myCar1.setSpeed(0);
		
		myCar1.upSpeed(30);
		
		System.out.println("�ڵ��� 1�� ������ " + myCar1.getColor() + "�̸�, ���� �ӵ��� " + myCar1.getSpeed() + "km �Դϴ�.");

	}

}
