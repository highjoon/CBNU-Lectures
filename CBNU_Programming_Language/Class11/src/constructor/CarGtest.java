package constructor;

class CarG {
	private String color;
	private int speed;
	
	CarG(String color, int speed) {		// �����ڿ� 2���� �Ķ���͸� ����.
		this.color = color;						// this�� ����Ͽ� �ʵ�� �Ķ���� ������ ����.
		this.speed = speed;
	}

	public String getColor() {
		return color;
	}

	public int getSpeed() {
		return speed;
	}	
}

public class CarGtest {

	public static void main(String[] args) {
		CarG myCar1 = new CarG("����", 0);	// �ν��Ͻ� (��ü) ������, 2���� �Ķ���͸� �Ѱ���.
		CarG myCar2 = new CarG("�Ķ�", 30);
		
		System.out.println("�ڵ��� 1�� ������ " + myCar1.getColor() + "�̸�, ����ӵ��� " + myCar1.getSpeed() + "km �Դϴ�.");
		System.out.println("�ڵ��� 2�� ������ " + myCar2.getColor() + "�̸�, ����ӵ��� " + myCar2.getSpeed() + "km �Դϴ�.");
	}

}
