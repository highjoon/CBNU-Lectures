package hw4;

// Payment 클래스.

public class Payment {

	public static String Payment(int pay) {
		
		// 결과를 나타내는 method 변수 초기화.
		String method = "결제전";
		
		// Passenger 클래스에서 선언한 pay 변수를 참조하여 다음과 같은 switch 문 진행.
		switch (pay) {
		
		case 1:
			method = "# 3. 카드로 결제한다.\n";
			break;
		
		case 2:
			method = "# 3. 현금으로 결제한다.\n";
			break;
		
		case 3:
			method = "# 3. 모바일로 결제한다.\n";
			break;
			
		default:
			method = "# 3. 랜덤으로 선택한다.\n";
		}
		
		// 결과값 반환.
		return method;
	}
}

