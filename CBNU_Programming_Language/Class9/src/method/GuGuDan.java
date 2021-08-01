package method;

import java.util.Scanner;

public class GuGuDan {

	public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in);
		int input = scanner.nextInt();
		
		GuGuDan ggd = new GuGuDan();
		ggd.gugudan(input);	

	}
	
	public void gugudan(int i) {
		
		for (int j = 1; j < 10; j++) {
			System.out.println(i + " * " + j + " = " + (i * j));
		}
	}

}
