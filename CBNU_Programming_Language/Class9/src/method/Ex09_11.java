package method;

import java.util.*;

public class Ex09_11 {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int coffee; 	// Ŀ�� ���� ���� ����.
		int ret;			// ��ȯ�� ���� ����.
		
		System.out.printf("� Ŀ�Ǹ� �帱���? (1: ����, 2: ����, 3: ��) ");
		coffee = s.nextInt();
		ret = coffee_machine(coffee);		// coffee_machine() �޼ҵ� ȣ�� // Ŀ�� �ӽ��� ��ư�� ������ �Ͱ� ���� ���.
		System.out.printf("�մ�~ Ŀ�� ���� �ֽ��ϴ�.\n");
		
		System.out.printf("� Ŀ�Ǹ� �帱���? (1: ����, 2: ����, 3: ��) ");
		coffee = s.nextInt();
		ret = coffee_machine(coffee);		// coffee_machine() �޼ҵ� ȣ�� // Ŀ�� �ӽ��� ��ư�� ������ �Ͱ� ���� ���.
		System.out.printf("�մ�~ Ŀ�� ���� �ֽ��ϴ�.\n");
		
		System.out.printf("� Ŀ�Ǹ� �帱���? (1: ����, 2: ����, 3: ��) ");
		coffee = s.nextInt();
		ret = coffee_machine(coffee);		// coffee_machine() �޼ҵ� ȣ�� // Ŀ�� �ӽ��� ��ư�� ������ �Ͱ� ���� ���.
		System.out.printf("�մ�~ Ŀ�� ���� �ֽ��ϴ�.\n");
			
	}
	
	public static int coffee_machine(int button) {
		
		// return ���� ���� �ڷ��� ���.
		// static ���� ���. ��� Ŭ�������� ���� ����. Ŭ���������� ����.
		
		System.out.printf("\n# 1. (�ڵ�����) �߰ſ� ���� �غ��Ѵ�.\n");
		System.out.printf("\n# 2. (�ڵ�����) �������� �غ��Ѵ�.\n");
		
		switch (button) {
		
		case 1:
			System.out.printf("# 3. (�ڵ�����) ����Ŀ�Ǹ� ź��.\n");
			break;
		
		case 2:
			System.out.printf("# 3. (�ڵ�����) ����Ŀ�Ǹ� ź��.\n");
			break;
		
		case 3:
			System.out.printf("# 3. (�ڵ�����) ��Ŀ�Ǹ� ź��.\n");
			break;
		
		default:
			System.out.printf("# 3. (�ڵ�����) �ƹ��ų� ź��.\n");
		}
		
		System.out.printf("# 4. (�ڵ�����) ���� �״´�.\n");
		System.out.printf("# 5. (�ڵ�����) ��Ǭ���� ��� ���δ�.\n\n");
		
		return 0;
	}

}
