//ÇÁ·Î±×·¥¸í: ¿¹Á¦ #5: È­¾¾ ¿Âµµ -> ¼·¾¾ ¿Âµµ º¯°æ
//ÀÛ¼ºÀÚ: À±»óÇÏ
//ÇÐ¹ø: 2020111597

import java.util.Scanner;

public class Fahrenheit {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner f = new Scanner(System.in);
		double fahrenheit, celsius;
		System.out.print("È­¾¾¿Âµµ: ");
		fahrenheit = f.nextDouble();
		
		celsius = (5.0/9.0) * (fahrenheit-32.0);
		System.out.println("¼·¾¾¿Âµµ: " + celsius);
	}

}
