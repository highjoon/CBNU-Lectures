// HW #3 : 년도를 입력하고 윤년인지 아닌지를 확인하는 프로그램
// 경영정보학과
// 2016024017
// 윤상준

import java.util.*;

public class LeapYearHW {

	public static void main(String[] args) {
		
		int year;
		String leap;
		
		System.out.println("===== 윤년 계산기 =====");
		System.out.println("\n");

		Scanner input = new Scanner(System.in);
		System.out.print("년도를 입력하세요 : ");
		year = input.nextInt();
		
		System.out.println("\n");
		
		if ((year % 4 == 0) && (year % 100 != 0)) {
			leap = "윤년";
			
		} else if ((year % 4 == 0) && (year % 100 == 0) && (year % 400 == 0)) {
			leap = "윤년";
			
		} else {
			leap = "평년";
		}
		
		System.out.println("입력한 " + year + "년은 " + leap + "입니다.");
		
		System.out.println("\n");
		System.out.println("===== 프로그램 종료 =====");

	}

}
