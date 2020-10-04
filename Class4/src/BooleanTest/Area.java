//프로그램명: 예제 #4: 원의 면적 구하기
//작성자: 윤상하
//학번: 2020111597

import java.util.Scanner;

public class Area {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		double radius, area;
		final double PI = 3.14;
		Scanner input = new Scanner(System.in);
		
		System.out.print("반지름을 입력하시오 : ");
		radius = input.nextInt();
		
		area = radius * radius * PI;
		System.out.println(area);
	}

}
