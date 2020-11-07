package hw5_2;

import java.util.Scanner;

public class CustomerManagement {
	public static void main (String[] args) {
		
		
		// Sccanner 기능을 사용하여 각 손님의 결제 금액을 수동적으로 입력함.
		Scanner input = new Scanner(System.in);
		
		// 3개의 Customer 객체를 선언.
		Customer customerLee = new Customer();
		Customer customerKim = new Customer();
		Customer customerPark = new Customer();
		
		// 각 객체는 결제 금액, 회원번호, 총 결제 금액, 회원등급, 회원등급에 따른 보너스 세일을 값으로 가짐.
		// showCustomerInfo() 메소드를 통해 모든 정보를 프린트함.
		customerLee.setCustomerName("LEE");
		System.out.print(customerLee.getCustomerName() + "님의 결제금액을 입력해주세요 : ");
		long price = input.nextLong();
		customerLee.setCustomerID(10101);
		customerLee.addSale(price);
		customerLee.gradeSet();
		customerLee.bonusSale();
		System.out.println(customerLee.showCustomerInfo());
		
		customerKim.setCustomerName("KIM");
		System.out.print(customerKim.getCustomerName() + "님의 결제금액을 입력해주세요 : ");
		int price1 = input.nextInt();
		customerKim.setCustomerID(10102);
		customerKim.addSale(price1);
		customerKim.gradeSet();
		customerKim.bonusSale();
		System.out.println(customerKim.showCustomerInfo());
		
		customerPark.setCustomerName("PARK");
		System.out.print(customerPark.getCustomerName() + "님의 결제금액을 입력해주세요 : ");
		int price2 = input.nextInt();
		customerPark.setCustomerID(10103);
		customerPark.addSale(price2);
		customerPark.gradeSet();
		customerPark.bonusSale();
		System.out.println(customerPark.showCustomerInfo());
	}
}

