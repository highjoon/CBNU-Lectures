package hw4;

// GetOff Ŭ����.

public class GetOff {

	public static String GetOff(int trans) {
		
		// ����� ��Ÿ���� out ���� �ʱ�ȭ.
		String out = "ž����";
		
		// Passenger Ŭ�������� ������ trans������ �����Ͽ� ������ ���� switch�� ����.
		switch (trans) {
		
		case 1:
			out = "# 5. �������� �����Ѵ�.\n";
			break;
		case 2:
			out = "# 5. ����ö���� �����Ѵ�.\n";
			break;
		case 3:
			out = "# 5. �ýÿ��� �����Ѵ�.\n";
			break;
				}
		
		// ����� ��ȯ.
		return out;
	}

}
