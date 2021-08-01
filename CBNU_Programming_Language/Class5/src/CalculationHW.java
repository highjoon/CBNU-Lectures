
public class CalculationHW {
	public static void main(String[] args) {
		
		// �濵�����а� 2016024017 ������
		
		// ������ �����Ͽ� ������� Ȯ���ϱ� ���� ���� �� ���� ���������� ������� �����Ͽ� �ּ����� ǥ����.
		
		// ���� i, j, h �� ���� ���Ƿ� ������.
		
		int i = 50;
		int j = 2;
		int h = 32;
		
		
		System.out.println("=== ��� ������ ===");					
		System.out.println("���� : " + (i + j));					// 52
		System.out.println("���� : " + (i - j));					// 48
		System.out.println("���� : " + (i * j));					// 100
		System.out.println("������ : " + (i / j));				// 25
		System.out.println("������ : " + (i % j));				// 0
		
		System.out.print("\n");										// �������� ���� �� ��Ʈ���� �ٹٲ� ����.
		
		System.out.println("=== �ڵ����� ������ ===");
		i++;																			// i ���� ���� ����� �� +1
		System.out.println("����1 : " + i);							// 51 (���� i���� 50�� ������ �ʴ� ������ 22�׿��� �̹� ++���� ����Ǿ��� ������ +1�� �Ǿ���. ���� 22�װ� 23�� �ڸ��� �ٲ� �����Ѵٸ� ���� i���� 50�� ��µ�.)
		j--;																			// j ���� ���� ����� �� -1
		System.out.println("����1 : " + j);							// 1 (���� j���� 1�� ������ ���� �̴��� 23�׿����� ������ ����.)
		++i;																			// i ���� ���� +1�� �� ���.
		System.out.println("����2 : " + i);							// 52 (23���� ���� �������� �̹� +1 �Ǿ� 51�� �Ǿ���, 26���� ���꿡�� �� +1�� �Ǿ����Ƿ� 52�� ��µ�.)
		--j;																			// j ���� ���� -1�� �� ���.
		System.out.println("����2 : " + j);						// 0 (0�� ������ ������ 27�׿����� ������ ����.)

		System.out.print("\n");
				
		System.out.println("=== �����, ���� ������ ===");			// i = 52, j = 0
		System.out.println("i == j >> " + (i == j));								// False
		System.out.println("i |= j >> " + (i != j));								// True
		System.out.println("i > j >> " + (i > j));									// True
		System.out.println("i < j >> " + (i < j));									// False	
		
		System.out.print("\n");
		
		System.out.println("=== ���� ������ ===");							// i = 52, j = 0
		System.out.println("&& (AND) >> " + (i > j && i > h));			// True
		System.out.println("&& (AND) >> " + (i > j && i < h));			// False
		System.out.println("|| (OR) >> " + (i > j || i < h));					// True
		System.out.println("|| (OR) >> " + (i > j || i > h));					// True
		
		System.out.print("\n");
		
		System.out.println("=== �Ҵ� ������ ===");
		System.out.println("h = " + h);												// ������ ���� h���� 32 ���.
		h = i;																							// h ������ ���ο� �� (i = 52)�� �Է������Ƿ� ������ h���� 32�� ���ŵǰ� ������ 52�� �Էµ�.
		System.out.println("h = " + h);												// 52

		System.out.print("\n");
				
		System.out.println("=== �ٿ� ���� ������ ===");
		i = i + 100;																				// ������ i ���� 52�� 100�� ���� ���� 152�� ���� i�� ���������Ƿ�, ������ i���� 52 ��� ������ 152�� �Էµ�.
		System.out.println("i = " + i);												// 152
		i = 11;																						// 57�׿��� ����� i���� 152 ��ſ� 11�� ���������Ƿ�, ������ i���� 152 ��ſ� ������ 11�� �Էµ�.
		System.out.println("i = " + i);												// 11
		i += 100;																					// Ǯ��� i = i + 100 �� �ǹǷ�, ������ ������ ������ ���� ������ i���� 11 + 100�� ����� 111�� ������ i������ �Էµ�.
		System.out.println("i = " + i);												// 111
		
	}

}