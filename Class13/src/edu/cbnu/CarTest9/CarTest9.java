package edu.cbnu.CarTest9;

public class CarTest9 {

	public static void main(String[] args) {
		
		Sedan sedan1 = new Sedan();
		sedan1.work();								// 오버라이딩 된 메소드를 호출 (Sedan 클래스에서)
		
		Truck truck1 = new Truck();
		truck1.work();								// 오버라이딩 된 메소드를 호출 (Truck 클래스에서)
	}

}
