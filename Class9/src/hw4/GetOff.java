package hw4;

public class GetOff {

	public static String GetOff(int trans) {
		
		String out = "탑승중";

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
		return out;
	}

}
