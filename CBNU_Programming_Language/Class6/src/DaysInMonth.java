import java.util.*;

public class DaysInMonth {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int month, days;
		
		Scanner input = new Scanner(System.in);
		System.out.print("일수를 알고 싶은 월을 입력하시오:");
		month = input.nextInt();
		
		switch (month) {
		case 4, 6, 9, 11:
			days = 30;
			break;
		case 2:
			days = 28;
			break;
		default:
			days = 31;
			break;
		}
		
		System.out.println("월의 날수는 " + days);
	}

}
