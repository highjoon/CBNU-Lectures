//프로그램명: 예제 #5: 마일->km 변경
//작성자: 윤상하
//학번: 2020111597

import java.util.Scanner;

public class Mile {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner m = new Scanner(System.in);
		double mile, km;
		System.out.print("마일을 입력하시오 : ");
		mile = m.nextDouble();
		
		km = mile * 1.609;
		System.out.println(mile + "마일은" + km +"킬로미터입니다.");
		
	}

}
