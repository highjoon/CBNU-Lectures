package hw4;

// Payment Ŭ����.

public class Payment {

	public static String Payment(int pay) {
		
		// ����� ��Ÿ���� method ���� �ʱ�ȭ.
		String method = "������";
		
		// Passenger Ŭ�������� ������ pay ������ �����Ͽ� ������ ���� switch �� ����.
		switch (pay) {
		
		case 1:
			method = "# 3. ī��� �����Ѵ�.\n";
			break;
		
		case 2:
			method = "# 3. �������� �����Ѵ�.\n";
			break;
		
		case 3:
			method = "# 3. ����Ϸ� �����Ѵ�.\n";
			break;
			
		default:
			method = "# 3. �������� �����Ѵ�.\n";
		}
		
		// ����� ��ȯ.
		return method;
	}
}

