package constructor;

class CarF {
	private String color;
	private int speed;
	
	CarF() {
		color = "빨강";
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
		
		System.out.println("자동차 1의 색상은 " + myCar1.getColor() + "이며, 현재속도는 " + myCar1.getSpeed() + "km 입니다.");
		System.out.println("자동차 2의 색상은 " + myCar2.getColor() + "이며, 현재속도는 " + myCar2.getSpeed() + "km 입니다.");
	}

}
