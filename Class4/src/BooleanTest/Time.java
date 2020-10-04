//프로그램명: 예제 #7: 초단위 입력 -> 시간 분 초 변경
//작성자: 윤상하
//학번: 2020111597

import java.util.Scanner;

public class Time {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner t = new Scanner(System.in);
		System.out.print("초를 입력하시오: ");
		int total = t.nextInt();
		
		System.out.println("**********************");
		
		int hour = total / 3600;
		int minute = total % 3600 / 60;
		int second = total % 3600 % 60;
		
		System.out.println(total + "초는" + hour + "시간" + minute + "분" + second + "초 입니다.");
	}

}
