package constructor;

class CarF {
	private String color;
	private int speed;
	
	CarF() {
		color = "����";
		speed = 0;
	}
	
	public String getColor() {
		return color;
	}
	
	public int getSpeed() {
		return speed;
	}
}

public class CarFtest {

	public static void main(String[] args) {
		CarF myCar1 = new CarF();
		CarF myCar2 = new CarF();
		
		System.out.println("�ڵ��� 1�� ������ " + myCar1.getColor() + "�̸�, ����ӵ��� " + myCar1.getSpeed() + "km �Դϴ�.");
		System.out.println("�ڵ��� 2�� ������ " + myCar2.getColor() + "�̸�, ����ӵ��� " + myCar2.getSpeed() + "km �Դϴ�.");
	}

}
