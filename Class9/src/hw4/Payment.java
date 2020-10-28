package hw4;

public class Payment {

	public static String Payment(int pay) {
		
		String method = "결제전";
		
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
		return method;
	}
}

