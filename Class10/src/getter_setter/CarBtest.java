package getter_setter;

public class CarBtest {

	public static void main(String[] args) {
		
		CarB myCar1 = new CarB();
		myCar1.color = "빨강";
		myCar1.speed = 0;
		
		myCar1.upSpeed(30);
		
		System.out.println("자동차 1의 색상은 " + myCar1.color + "이며, 현재속도는 " + myCar1.speed + "km 입니다.");
		
		System.out.println("자동차 1의 색상은 " + myCar1.getColor() + "이며, 현재속도는 " + myCar1.getSpeed() + "km 입니다.");
	}

}
