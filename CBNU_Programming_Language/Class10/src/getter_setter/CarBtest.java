package getter_setter;

public class CarBtest {

	public static void main(String[] args) {
		
		CarB myCar1 = new CarB();
		myCar1.color = "����";
		myCar1.speed = 0;
		
		myCar1.upSpeed(30);
		
		System.out.println("�ڵ��� 1�� ������ " + myCar1.color + "�̸�, ����ӵ��� " + myCar1.speed + "km �Դϴ�.");
		
		System.out.println("�ڵ��� 1�� ������ " + myCar1.getColor() + "�̸�, ����ӵ��� " + myCar1.getSpeed() + "km �Դϴ�.");
	}

}
