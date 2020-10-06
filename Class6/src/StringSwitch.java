import java.util.*;

public class StringSwitch {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		String month;
		int monthnumber;
		
		Scanner input = new Scanner(System.in);
		System.out.print("월의 이름을 입력하시오:");
		month = input.next();
		
		switch (month) {
		case "january":
			monthnumber = 1;
			break;
		case "febuary":
			monthnumber = 2;
			break;
		case "march":
			monthnumber = 3;
			break;
		default:
			monthnumber = 0;
			break;
		}
		
		System.out.println(monthnumber);
	}

}
