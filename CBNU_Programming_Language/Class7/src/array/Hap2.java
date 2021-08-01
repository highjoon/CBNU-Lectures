package array;
import java.util.*;

public class Hap2 {

	public static void main(String[] args) {
		
		int a,b,c,d,e,f,g,h,i,j;
		int hap = 0;
		
		Scanner input = new Scanner(System.in);
		
		System.out.printf("정수 a 입력 : ");
		a = input.nextInt();
		
		System.out.printf("정수 b 입력 : ");
		b = input.nextInt();
		
		System.out.printf("정수 c 입력 : ");
		c = input.nextInt();
		
		System.out.printf("정수 d 입력 : ");
		d = input.nextInt();
		
		System.out.printf("정수 e 입력 : ");
		e = input.nextInt();

		System.out.printf("정수 f 입력 : ");
		f = input.nextInt();

		System.out.printf("정수 g 입력 : ");
		g = input.nextInt();

		System.out.printf("정수 h 입력 : ");
		h = input.nextInt();

		System.out.printf("정수 i 입력 : ");
		i = input.nextInt();

		System.out.printf("정수 j 입력 : ");
		j = input.nextInt();
		
		hap = a + b + c+ d + e + f + g + h + i + j;
		
		System.out.println("합은 : " + hap + "입니다.");

	}

}
