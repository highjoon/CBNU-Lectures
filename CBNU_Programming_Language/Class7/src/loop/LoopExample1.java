package loop;

import java.util.Scanner;

public class LoopExample1 {

	public static void main(String[] args) {
		Scanner  input = new Scanner (System.in);
		System.out.print("������ �߿��� ����ϰ���� ���� �Է��Ͻÿ�: ");
		int dan = input.nextInt();
		int i = 1;
		while (i < 10) {
			System.out.println(dan + " * " + i + " = " + (dan * i));
			i++;
		}
		

	}

}
