package array;
import java.util.Scanner;

public class ArrayTest2 {

	public static void main(String[] args) {
		int [] scores = new int [5];
		int total = 0;
		Scanner scan = new Scanner(System.in);
		
		for (int i = 0; i < scores.length; i++) {
			System.out.print("������ �Է��ϼ��� : ");
			scores[i] = scan.nextInt();
		}
		
		for (int j = 0; j < scores.length; j++) {
			total += scores[j];
		}
		
		System.out.println("��� ������ " + total/scores.length + "�Դϴ�.");
	}

}
