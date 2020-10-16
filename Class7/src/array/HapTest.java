package array;
import java.util.*;

public class HapTest {

	public static void main(String[] args) {
		
		Scanner input = new Scanner(System.in);
		int [] list = new int[100];
		int hap = 0;
		int i, j;
		
		for (i = 1; i <= 100; i++) {
			System.out.printf(i + " 번째 정수를 입력하세요 : ");
			list[i] = input.nextInt();
		}
		
		for (j = 1; j <= 100; j++ ) {
			hap = hap + list[j];
		}
		
		System.out.printf("합계는 : %d 입니다.", hap);
		
	}

}
