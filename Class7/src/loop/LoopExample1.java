package loop;

import java.util.Scanner;

public class LoopExample1 {

	public static void main(String[] args) {
		Scanner  input = new Scanner (System.in);
		System.out.print("구구단 중에서 출력하고싶은 단을 입력하시오: ");
		int dan = input.nextInt();
		int i = 1;
		while (i < 10) {
			System.out.println(dan + " * " + i + " = " + (dan * i));
			i++;
		}
		

	}

}
