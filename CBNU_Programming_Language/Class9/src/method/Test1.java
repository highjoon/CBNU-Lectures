package method;

public class Test1 {

	public static void main(String[] args) {
		
		int sum = 0;
		int result = 0;
		
		for (int i = 0; i <= 10; i++) {
			sum += i;
		}
		
		System.out.println("1���� 10������ ������ ���� " + sum + "�Դϴ�.");
		
		result = sum % 2;
		if (result == 0) {
			System.out.println("¦�� �Դϴ�.");
		} else {
			System.out.println("Ȧ�� �Դϴ�.");
		}

	}

}
