import java.util.*;

public class Score2Grade {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int score, number;
		char grade;
		
		Scanner input = new Scanner(System.in);
		System.out.print("������ �Է��Ͻÿ�:");
		score = input.nextInt();
		number = score / 10;
		
		switch(number) {
		case 10:
		case 9:
			grade = 'A';
			break;
		case 8:
			grade = 'B';
			break;
		case 7:
			grade = 'C';
			break;
		case 6:
			grade = 'D';
			break;
		default:
			grade = 'F';
			break;
		}
		
		System.out.println("����:" + grade);
	}

}
