package loop;

import java.util.Scanner;

public class Divisor {

	public static void main(String[] args) {
		Scanner input = new Scanner (System.in);
		int num;
		System.out.print("���� ������ �Է��Ͻÿ� : ");
		num = input.nextInt();
		
		System.out.println(num + "�� ����� ������ �����ϴ�.");
		for (int i = 1; i <= num; i++) {
			if (num % i == 0) {
				System.out.print(" " + i);
			}
		}
	}

}
