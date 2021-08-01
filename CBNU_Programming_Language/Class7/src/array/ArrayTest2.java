package array;
import java.util.Scanner;

public class ArrayTest2 {

	public static void main(String[] args) {
		int [] scores = new int [5];
		int total = 0;
		Scanner scan = new Scanner(System.in);
		
		for (int i = 0; i < scores.length; i++) {
			System.out.print("성적을 입력하세요 : ");
			scores[i] = scan.nextInt();
		}
		
		for (int j = 0; j < scores.length; j++) {
			total += scores[j];
		}
		
		System.out.println("평균 성적은 " + total/scores.length + "입니다.");
	}

}
