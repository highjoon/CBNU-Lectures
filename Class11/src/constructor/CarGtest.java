package constructor;

class CarG {
	private String color;
	private int speed;
	
	CarG(String color, int speed) {		// 생성자에 2개의 파라미터를 받음.
		this.color = color;						// this를 사용하여 필드와 파라미터 변수를 구분.
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
		CarG myCar1 = new CarG("빨강", 0);	// 인스턴스 (객체) 생성시, 2개의 파라미터를 넘겨줌.
		CarG myCar2 = new CarG("파랑", 30);
		
		System.out.println("자동차 1의 색상은 " + myCar1.getColor() + "이며, 현재속도는 " + myCar1.getSpeed() + "km 입니다.");
		System.out.println("자동차 2의 색상은 " + myCar2.getColor() + "이며, 현재속도는 " + myCar2.getSpeed() + "km 입니다.");
	}

}
