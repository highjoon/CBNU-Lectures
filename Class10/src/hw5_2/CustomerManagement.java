package hw5_2;

import java.util.Scanner;

public class CustomerManagement {
	public static void main (String[] args) {
		
		Scanner input = new Scanner(System.in);
		
		Customer customerLee = new Customer();
		Customer customerKim = new Customer();
		Customer customerPark = new Customer();
		
		
		customerLee.setCustomerName("LEE");
		System.out.print(customerLee.getCustomerName() + "님의 결제급액을 입력해주세요 : ");
		long price = input.nextLong();
		customerLee.setCustomerID(10101);
		customerLee.addSale(price);
		customerLee.gradeSet();
		customerLee.bonusSale();
		System.out.println(customerLee.showCustomerInfo());
		
		customerKim.setCustomerName("KIM");
		System.out.print(customerKim.getCustomerName() + "님의 결제급액을 입력해주세요 : ");
		int price1 = input.nextInt();
		customerKim.setCustomerID(10102);
		customerKim.addSale(price1);
		customerKim.gradeSet();
		customerKim.bonusSale();
		System.out.println(customerKim.showCustomerInfo());
		
		customerPark.setCustomerName("PARK");
		System.out.print(customerPark.getCustomerName() + "님의 결제급액을 입력해주세요 : ");
		int price2 = input.nextInt();
		customerPark.setCustomerID(10103);
		customerPark.addSale(price2);
		customerPark.gradeSet();
		customerPark.bonusSale();
		System.out.println(customerPark.showCustomerInfo());
	}
}

