import java.util.Scanner; // Scanner Ŭ���� ����

public class Add2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner input = new Scanner(System.in);
		int x; // ù ��° ���� ����
		int y; // �� ��° ���� ����
		int sum; // ���� ����
		
		System.out.print("ù��° ���ڸ� �Է��Ͻÿ�. : "); // �Է� �ȳ� ���
		x = input.nextInt(); // ����ڷκ��� ù ��° ���ڸ� �д´�.
		
		System.out.print("�ι�° ���ڸ� �Է��Ͻÿ�. : "); // �Է� �ȳ� ���
		y = input.nextInt(); // ����ڷκ��� �� ��° ���ڸ� �д´�.
		
		sum = x + y; // �� ���� ���ڸ� ���Ѵ�.
		
		System.out.println(sum); // ���� ����Ѵ�.
	}

}
