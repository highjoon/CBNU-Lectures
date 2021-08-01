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
			
			System.out.print("원하시는 좌석번호를 입력하세요 (종료는 -1) : " );
			num = input.nextInt();
			if (num == -1) {
				System.out.println("종료되었습니다.");
				break;
			} else if (seats[num-1] == 0) {
					seats[num-1] = 1;
					System.out.println("\n" + "예약되었습니다." + "\n");
					} else {
						System.out.println("이미 예약된 자리입니다."+ "\n");
				}
			}
			
		}

	

}
