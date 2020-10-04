//프로그램명: 예제 #3: 연봉 계산 문제
//작성자: 윤상하
//학번: 2020111597

import java.util.Scanner;

public class AnnualIncome {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int salary;
		int saving;
		Scanner input = new Scanner(System.in);
		
		System.out.print("월급을 입력하시오 : ");
		salary = input.nextInt();
		
		saving = salary * 12 * 10;
		System.out.println("10년 동안의 저축액: "+saving);
	}

}
