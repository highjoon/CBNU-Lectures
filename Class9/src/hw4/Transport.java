package hw4;

public class Transport {
		

	public static String Transport(int trans) {
		
		String getIn = "탑승전";
		
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
		return getIn;
	}
}

