package edu.cbnu.multiple_inheritance;

 interface Car {																		// Car 인터페이스 생성.
	 abstract void work();														// 모두 추상 메소드이므로 abstract는 생략 가능.
}
 
 interface Cannon {																// Cannon 인터페이스 생성.
	 void fire();																			// abstract 생략.
 }

 class Tank implements Car, Cannon {								// implement를 사용. (Car와 Cannon 인터페이스를 다중상속으로 구현)
	 public void work() {																// interface의 추상메소드를 완성할때는 public 키워드를 붙임.
		 System.out.println("탱크가 전진합니다.");
	 }
	 
	 public void fire() {																// 오버라이딩.
		 System.out.println("탱크가 포를 발사합니다.");
	 }
 }