//프로그램명: 예제 #2: Scanner를 이용한 키 입력 연습
//작성자: 윤상하
//학번: 2020111597

import java.util.Scanner;

public class Height {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner data = new Scanner(System.in);
		System.out.println("나이, 체중, 신장을 빈칸으로 분리하여 순서대로 입력하세요");
		int age;
		double weight, tall;
		age = data.nextInt();
		weight = data.nextDouble();
		tall = data.nextDouble();
		
		System.out.println("당신의 나이는 " + age + "살입니다.");
		System.out.println("당신의 체중은 " + weight + "kg입니다.");
		System.out.println("당신의 신장은 " + tall + "cm입니다.");
		
	}
}
