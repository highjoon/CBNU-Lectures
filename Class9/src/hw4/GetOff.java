package hw4;

// GetOff 클래스.

public class GetOff {

	public static String GetOff(int trans) {
		
		// 결과를 나타내는 out 변수 초기화.
		String out = "탑승중";
		
		// Passenger 클래스에서 선언한 trans변수를 참조하여 다음과 같은 switch문 진행.
		switch (trans) {
		
		case 1:
			out = "# 5. 버스에서 하차한다.\n";
			break;
		case 2:
			out = "# 5. 지하철에서 하차한다.\n";
			break;
		case 3:
			out = "# 5. 택시에서 하차한다.\n";
			break;
				}
		
		// 결과값 반환.
		return out;
	}

}
