package hw4;

// Transport 클래스.

public class Transport {
		

	public static String Transport(int trans) {
		
		// 결과값 변수 getIn 초기화.
		String getIn = "탑승전";
		
		// Passenger 클래스에서 선언한 trans 변수를 참조하여 다음과 같은 switch 문 진행.
		switch (trans) {
		case 1:
			getIn = "# 2. 버스에 탑승한다.\n";
			break;
		case 2:
			getIn = "# 2. 지하철에 탑승한다.\n";
			break;
		case 3:
			getIn = "# 2. 택시에 탑승한다.\n";
			break;
		default:
			getIn = "# 2. 가장 가까운 곳에 있는 교통수단을 사용한다.\n";
			break;
		}
		
		// 결과값 반환.
		return getIn;
	}
}

