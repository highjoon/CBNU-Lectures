package array;
import java.util.Scanner;

public class HeightAve {

	public static void main(String[] args) {
		String [] name = { "����", "ö��", "�浿", "����", "����" };
		Scanner height = new Scanner(System.in);
		int sum = 0;
		int avg = 0;
		int height_list [] = new int [5];
		int tallest = height_list[0];
		int smallest= height_list[0];
		int smallIndex = 0;
		int tallIndex = 0;
		
		for (int i = 0; i < name.length; i++) {
			System.out.print(name[i] + "�� Ű�� �Է��ϼ��� : ");
			height_list[i] = height.nextInt();
			sum += height_list[i];
		}
		
		avg = sum / name.length;
		
		for (int g = 0; g < name.length; g++) {
			if (height_list[g] > tallest) {
				tallest = height_list[g];
				tallIndex = g;
			}
		}

		smallest = tallest;
//		??
		
		for (int h = 1; h < name.length; h++) {
			if (height_list[h] < smallest) {
				smallest = height_list[h];
				smallIndex = h;
			}
			
		}
		
		System.out.println("���ġ�� " + avg + "�Դϴ�.");
		System.out.println("���� ū �л��� " + name[tallIndex] + "�Դϴ�.");
		System.out.println("���� ���� �л��� " + name[smallIndex] + "�Դϴ�.");
	}

}
