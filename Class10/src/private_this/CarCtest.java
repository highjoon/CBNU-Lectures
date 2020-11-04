package private_this;

public class CarCtest {

	public static void main(String[] args) {
		
		CarC myCar1 = new CarC();
		myCar1.setColor("빨강");
		myCar1.setSpeed(0);
		
		myCar1.upSpeed(30);
		
		System.out.println("자동차 1의 색상은 " + myCar1.getColor() + "이며, 현재 속도는 " + myCar1.getSpeed() + "km 입니다.");

	}

}
