import java.util.*;

public class DaysInMonth {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int month, days;
		
		Scanner input = new Scanner(System.in);
		System.out.print("�ϼ��� �˰� ���� ���� �Է��Ͻÿ�:");
		month = input.nextInt();
		
		switch (month) {
		case 4, 6, 9, 11:
			days = 30;
			break;
		case 2:
			days = 28;
			break;
		default:
			days = 31;
			break;
		}
		
		System.out.println("���� ������ " + days);
	}

}
