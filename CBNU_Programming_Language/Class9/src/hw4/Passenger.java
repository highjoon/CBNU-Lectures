package hw4;

// main �޼ҵ带 ����Ͽ� ��ü���� �������� ��ȯ.
// Passenger Ŭ����. (Main() �޼ҵ�)
// GetOff Ŭ����. (������� ���� �޼ҵ�)
// Payment Ŭ����. (�������� ���� �޼ҵ�)
// Transport Ŭ����. (������� ���� �޼ҵ�)
// �� 4���� Ŭ������ �����Ͽ� �ۼ�.
// main() �޼ҵ尡 �ִ� Passenger Ŭ�������� ������ 3���� Ŭ������ �����Ͽ� ����.

import java.util.*;

// Passenger Ŭ����

public class Passenger {

	public static void main(String[] args) {
		
		// main �޼ҵ�
		
		Scanner s = new Scanner(System.in);
		int trans;
		int pay;
		
		System.out.printf("� ��������� �̿��Ͻðڽ��ϱ�? (1: ����, 2: ����ö, 3: �ý�) : ");
		trans = s.nextInt();
		
		System.out.printf("\n# 1. ���������� �̵��Ѵ�.\n");
		
		// Transport Ŭ������ Transport �޼ҵ� ����.
		System.out.println(Transport.Transport(trans));
		
		System.out.printf("� ���������� �̿��Ͻðڽ��ϱ�? (1: ī��, 2: ����, 3: �����) : ");
		pay = s.nextInt();
		
		// Payment Ŭ������ Payment �޼ҵ� ����.
		System.out.println(Payment.Payment(pay));
		
		System.out.printf("# 4. ������ �Ϸ��Ѵ�.\n");
		
		// GetOff Ŭ������ GetOff �޼ҵ� ����.
		System.out.println(GetOff.GetOff(trans));
		
		System.out.printf("�������� �����߽��ϴ�.\n");
	}
}
