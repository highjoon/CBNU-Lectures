package array;
import java.util.Scanner;

public class TheaterReserve {

	public static void main(String[] args) {
		final int size = 10;
		int seats [] = new int [10];
		Scanner input = new Scanner(System.in);
		int num;
		
		while (true) {
			System.out.println("-------------------------------");
			
			for (int i = 0; i < size; i++) {
				System.out.print((i + 1) + " ");
			}
			
			System.out.println("\n-------------------------------");
			
			for (int i = 0; i < size; i++) {
				System.out.print(seats[i] + " ");
			}
			
			System.out.println("\n-------------------------------\n");
			
			System.out.print("���Ͻô� �¼���ȣ�� �Է��ϼ��� (����� -1) : " );
			num = input.nextInt();
			if (num == -1) {
				System.out.println("����Ǿ����ϴ�.");
				break;
			} else if (seats[num-1] == 0) {
					seats[num-1] = 1;
					System.out.println("\n" + "����Ǿ����ϴ�." + "\n");
					} else {
						System.out.println("�̹� ����� �ڸ��Դϴ�."+ "\n");
				}
			}
			
		}

	

}
