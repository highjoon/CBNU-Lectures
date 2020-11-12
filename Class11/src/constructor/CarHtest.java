package constructor;

class CarH {
	private String color;
	private int speed;
	
	CarH() {}											// 파라미터 개수가 다른 동일한 이름의 생성자 (1).
	
	CarH(String color) {							// 파라미터 개수가 다른 동일한 이름의 생성자 (2).
		this.color = color;
	}
	
	CarH(String color, int speed) {		// 파라미터 개수가 다른 동일한 이름의 생성자 (3).
		this.color = color;
		this.speed = speed;
	}
	
	public String getColor() {
		return color;
	}
	
	public int getSpeed() {
		return speed;
	}
}

public class CarHtest {

	public static void main(String[] args) {
		CarH myCar1 = new CarH();					// 객체를 만들 때 각각 다른 생성자를 호출.
		CarH myCar2 = new CarH("빨강");
		CarH myCar3 = new CarH("파랑", 30);
		
		System.out.println("자동차 1의 색상은 " + myCar1.getColor() + "이며, 현재속도는 " + myCar1.getSpeed() + "km 입니다.");
		System.out.println("자동차 2의 색상은 " + myCar2.getColor() + "이며, 현재속도는 " + myCar2.getSpeed() + "km 입니다.");
		System.out.println("자동차 3의 색상은 " + myCar3.getColor() + "이며, 현재속도는 " + myCar3.getSpeed() + "km 입니다.");
	}

}
