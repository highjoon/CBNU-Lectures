//프로그램명: 예제 #6: 부가세 및 잔돈 구하기
//작성자: 윤상하
//학번: 2020111597

import java.util.Scanner;

public class Money {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner m = new Scanner(System.in);
		int receive, total, surtax, change;
		System.out.print("받은돈: ");
		receive = m.nextInt();
		System.out.print("상품의 총액: ");
		total = m.nextInt();
		System.out.println("************************");
		
		surtax = total * 10 / 100;
		change = receive - total;
		
		System.out.println("부가세: " + surtax);
		System.out.println("잔돈: " + change);
		
	}

}
