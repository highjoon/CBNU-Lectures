package array;
import java.util.*;

public class HapTest {

	public static void main(String[] args) {
		
		Scanner input = new Scanner(System.in);
		int [] list = new int[100];
		int hap = 0;
		int i, j;
		
		for (i = 1; i <= 100; i++) {
			System.out.printf(i + " ��° ������ �Է��ϼ��� : ");
			list[i] = input.nextInt();
		}
		
		for (j = 1; j <= 100; j++ ) {
			hap = hap + list[j];
		}
		
		System.out.printf("�հ�� : %d �Դϴ�.", hap);
		
	}

}
