// HW #3 : 년도를 입력하고 윤년인지 아닌지를 확인하는 프로그램
// 경영정보학과
// 2016024017
// 윤상준

import java.util.*;	// Scanner 기능을 사용하기 위해 util 패키지를 import 한다.

public class LeapYearHW {	// LeapYearHW 라는 이름의 클래스를 선언한다.

	public static void main(String[] args) {
		
		int year;		// 년도를 입력하기 위한 변수 year을 선언한다. 년도는 정수로 이루어져있으므로 int형으로 선언한다.
		String leap;	// 윤년 여부를 판별하기 위한 변수 leap을 선언한다. "윤년" 또는 "평년"으로 입력할 예정이므로 String형으로 선언한다.
		
		System.out.println("===== 윤년 계산기 =====");	// 가독성을 위해 프로그램의 제목을 먼저 표시한다.
		System.out.println("\n");					// 가독성을 위해 한줄 띄어쓰기를 선언한다.

		Scanner input = new Scanner(System.in);	// 년도를 입력받기 위한 Scanner input 변수를 선언한다.
		System.out.print("년도를 입력하세요 : ");		// 년도를 입력받기 위해 입력 코드를 호출한다.
		year = input.nextInt();					// 입력받은 년도를 앞서 선언한 year 변수에 저장한다.
		
		System.out.println("\n");				// 가독성을 위해 한줄 띄어쓰기를 선언한다.
		
		// 각 조건을 더욱 세세하게 설정할 수 있으므로 If, Else 조건문 형식을 이용한다.
		
		// 4로 나누어 떨어지면서 100으로 나누어 떨어지면 평년 이라는 조건을 응용하여,
		// 4로 나누어 떨어지면서 100으로 나누어 떨어지지 않는 년도는 윤년 이라는 조건을 설정한다.
		// 결과값은  leap 변수에 저장한다.
		if ((year % 4 == 0) && (year % 100 != 0)) {		
			leap = "윤년";
			
		// 4, 100, 400으로 나누어 떨어지면 윤년 이라는 조건을 설정한다.
		// 결과값은  leap 변수에 저장한다.
		} else if ((year % 4 == 0) && (year % 100 == 0) && (year % 400 == 0)) {
			leap = "윤년";
		
		// 상위 조건을 만족하지 않는 년도는 모두 평년이므로, else 조건으로 평년 여부를 설정한다.
		// 결과값은  leap 변수에 저장한다.
		} else {
			leap = "평년";
		}
		
		// 윤년, 평년 판별 여부를 표시하기 위한 print문을 설정한다.
		// 앞서 저장한 year (입력한 년도), leap (윤년, 평년 여부) 변수를 사용한다.
		System.out.println("입력한 " + year + "년은 " + leap + "입니다.");
		
		
		System.out.println("\n"); 						// 가독성을 위해 한줄 띄어쓰기를 선언한다.
		System.out.println("===== 프로그램 종료 ====="); 		// 프로그램이 종료되었음을 표시한다.

		
		
		
	}

}
