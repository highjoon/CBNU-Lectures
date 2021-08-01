package method;

import java.util.*;

public class Ex09_11 {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int coffee; 	// 커피 종류 변수 선언.
		int ret;			// 반환값 변수 선언.
		
		System.out.printf("어떤 커피를 드릴까요? (1: 보통, 2: 설탕, 3: 블랙) ");
		coffee = s.nextInt();
		ret = coffee_machine(coffee);		// coffee_machine() 메소드 호출 // 커피 머신의 버튼을 누르는 것과 같은 기능.
		System.out.printf("손님~ 커피 여기 있습니다.\n");
		
		System.out.printf("어떤 커피를 드릴까요? (1: 보통, 2: 설탕, 3: 블랙) ");
		coffee = s.nextInt();
		ret = coffee_machine(coffee);		// coffee_machine() 메소드 호출 // 커피 머신의 버튼을 누르는 것과 같은 기능.
		System.out.printf("손님~ 커피 여기 있습니다.\n");
		
		System.out.printf("어떤 커피를 드릴까요? (1: 보통, 2: 설탕, 3: 블랙) ");
		coffee = s.nextInt();
		ret = coffee_machine(coffee);		// coffee_machine() 메소드 호출 // 커피 머신의 버튼을 누르는 것과 같은 기능.
		System.out.printf("손님~ 커피 여기 있습니다.\n");
			
	}
	
	public static int coffee_machine(int button) {
		
		// return 값과 같은 자료형 사용.
		// static 변수 사용. 모든 클래스에서 공유 가능. 클래스명으로 선언.
		
		System.out.printf("\n# 1. (자동으로) 뜨거운 물을 준비한다.\n");
		System.out.printf("\n# 2. (자동으로) 종이컵을 준비한다.\n");
		
		switch (button) {
		
		case 1:
			System.out.printf("# 3. (자동으로) 보통커피를 탄다.\n");
			break;
		
		case 2:
			System.out.printf("# 3. (자동으로) 설탕커피를 탄다.\n");
			break;
		
		case 3:
			System.out.printf("# 3. (자동으로) 블랙커피를 탄다.\n");
			break;
		
		default:
			System.out.printf("# 3. (자동으로) 아무거나 탄다.\n");
		}
		
		System.out.printf("# 4. (자동으로) 물을 붓는다.\n");
		System.out.printf("# 5. (자동으로) 스푼으로 저어서 녹인다.\n\n");
		
		return 0;
	}

}
