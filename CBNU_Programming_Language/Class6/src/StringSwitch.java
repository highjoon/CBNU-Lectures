import java.util.*;

public class StringSwitch {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		String month;
		int monthnumber;
		
		Scanner input = new Scanner(System.in);
		System.out.print("���� �̸��� �Է��Ͻÿ�:");
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
