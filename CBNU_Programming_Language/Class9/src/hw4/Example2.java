package hw4;

//��������� �̿��Ͽ� ���������� �̵��ϴ� �������� �ۼ�.
//1. ������� �̿� (����, ����ö, �ý�).
//2. �������� ���� (ī��, ����, �����).
//ž���� ������ܿ��� ����.
//������ ����.
//������ ����.
//�������� �������� �� 3���� ����. (�Ȱ��� �ڵ��� 3�� �ݺ�)

import java.util.*;

public class Example2 {

	public static void main(String[] args) {
		
		Scanner s = new Scanner(System.in);
		int trans;
		int pay;
		
		// ������� ����
		// switch �� ���.
		
		System.out.printf("� ��������� �̿��Ͻðڽ��ϱ�? (1: ����, 2: ����ö, 3: �ý�) ");
		trans = s.nextInt();
		
		System.out.printf("\n# 1. ���������� �̵��Ѵ�.\n");
		
		switch (trans) {
		
		case 1:
			System.out.printf("# 2. ������ ž���Ѵ�.\n");
			break;
		case 2:
			System.out.printf("# 2. ����ö�� ž���Ѵ�.\n");
			break;
		case 3:
			System.out.printf("# 2. �ýÿ� ž���Ѵ�.\n");
			break;
		default:
			System.out.printf("# 2. ���� ����� ���� �ִ� ��������� ����Ѵ�.\n");
			break;
		}

		
		// �������� ����
		// switch �� ���.
		
		System.out.printf("� ���������� �̿��Ͻðڽ��ϱ�? (1: ī��, 2: ����, 3: �����) ");
		pay = s.nextInt();
		
		switch (pay) {
			
		case 1:
			System.out.printf("# 3. ī��� �����Ѵ�.\n");
			break;
		
		case 2:
			System.out.printf("# 3. �������� �����Ѵ�.\n");
			break;
		
		case 3:
			System.out.printf("# 3. ����Ϸ� �����Ѵ�.\n");
			break;
			
		default:
			System.out.printf("# 3. �������� �����Ѵ�.\n");
		}
		
		System.out.printf("# 4. ������ �Ϸ��Ѵ�.\n");

		switch (trans) {
				
				case 1:
					System.out.printf("# 5. �������� �����Ѵ�.\n");
					break;
				case 2:
					System.out.printf("# 5. ����ö���� �����Ѵ�.\n");
					break;
				case 3:
					System.out.printf("# 5. �ýÿ��� �����Ѵ�.\n");
					break;
				}
		
		//������ ����.
		
		System.out.printf("�������� �����߽��ϴ�.\n");
		
		System.out.printf("� ��������� �̿��Ͻðڽ��ϱ�? (1: ����, 2: ����ö, 3: �ý�) ");
		trans = s.nextInt();
		
		System.out.printf("\n# 1. ���������� �̵��Ѵ�.\n");
		
		switch (trans) {
		
		case 1:
			System.out.printf("# 2. ������ ž���Ѵ�.\n");
			break;
		case 2:
			System.out.printf("# 2. ����ö�� ž���Ѵ�.\n");
			break;
		case 3:
			System.out.printf("# 2. �ýÿ� ž���Ѵ�.\n");
			break;
		default:
			System.out.printf("# 2. ���� ����� ���� �ִ� ��������� ����Ѵ�.\n");
			break;
		}
		
		System.out.printf("� ���������� �̿��Ͻðڽ��ϱ�? (1: ī��, 2: ����, 3: �����) ");
		pay = s.nextInt();
		
		switch (pay) {
			
		case 1:
			System.out.printf("# 3. ī��� �����Ѵ�.\n");
			break;
		
		case 2:
			System.out.printf("# 3. �������� �����Ѵ�.\n");
			break;
		
		case 3:
			System.out.printf("# 3. ����Ϸ� �����Ѵ�.\n");
			break;
			
		default:
			System.out.printf("# 3. �������� �����Ѵ�.\n");
		}
		
		System.out.printf("# 4. ������ �Ϸ��Ѵ�.\n");

		switch (trans) {
				
				case 1:
					System.out.printf("# 5. �������� �����Ѵ�.\n");
					break;
				case 2:
					System.out.printf("# 5. ����ö���� �����Ѵ�.\n");
					break;
				case 3:
					System.out.printf("# 5. �ýÿ��� �����Ѵ�.\n");
					break;
				}
		
		System.out.printf("�������� �����߽��ϴ�.\n");
		
		System.out.printf("� ��������� �̿��Ͻðڽ��ϱ�? (1: ����, 2: ����ö, 3: �ý�) ");
		trans = s.nextInt();
		
		System.out.printf("\n# 1. ���������� �̵��Ѵ�.\n");
		
		switch (trans) {
		
		case 1:
			System.out.printf("# 2. ������ ž���Ѵ�.\n");
			break;
		case 2:
			System.out.printf("# 2. ����ö�� ž���Ѵ�.\n");
			break;
		case 3:
			System.out.printf("# 2. �ýÿ� ž���Ѵ�.\n");
			break;
		default:
			System.out.printf("# 2. ���� ����� ���� �ִ� ��������� ����Ѵ�.\n\n");
			break;
		}
		
		System.out.printf("� ���������� �̿��Ͻðڽ��ϱ�? (1: ī��, 2: ����, 3: �����) ");
		pay = s.nextInt();
		
		switch (pay) {
			
		case 1:
			System.out.printf("# 3. ī��� �����Ѵ�.\n");
			break;
		
		case 2:
			System.out.printf("# 3. �������� �����Ѵ�.\n");
			break;
		
		case 3:
			System.out.printf("# 3. ����Ϸ� �����Ѵ�.\n");
			break;
			
		default:
			System.out.printf("# 3. �������� �����Ѵ�.\n");
		}
		
		System.out.printf("# 4. ������ �Ϸ��Ѵ�.\n");

		switch (trans) {
				
				case 1:
					System.out.printf("# 5. �������� �����Ѵ�.\n");
					break;
				case 2:
					System.out.printf("# 5. ����ö���� �����Ѵ�.\n");
					break;
				case 3:
					System.out.printf("# 5. �ýÿ��� �����Ѵ�.\n");
					break;
				}
		
		System.out.printf("�������� �����߽��ϴ�.\n\n");

	}
	
}
