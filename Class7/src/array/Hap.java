package array;
import java.util.*;

public class Hap {

	public static void main(String[] args) {
		
		int a, b, c, d;
		int sum = 0;
		
		Scanner input = new Scanner(System.in);
		
		System.out.printf("정수 a 입력 : ");
		a = input.nextInt();
		
		System.out.printf("정수 b 입력 : ");
		b = input.nextInt();
		
		System.out.printf("정수 c 입력 : ");
		c = input.nextInt();
		
		System.out.printf("정수 d 입력 : ");
		d = input.nextInt();
		
		sum = a + b + c+ d;
		
		System.out.println("합은 : " + sum + "입니다.");

	}

}
