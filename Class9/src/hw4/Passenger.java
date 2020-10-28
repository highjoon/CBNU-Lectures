package hw4;

import java.util.*;

public class Passenger {

	public static void main(String[] args) {
		
		Scanner s = new Scanner(System.in);
		int trans;
		int pay;
		
		System.out.printf("어떤 교통수단을 이용하시겠습니까? (1: 버스, 2: 지하철, 3: 택시) : ");
		trans = s.nextInt();
		
		System.out.printf("\n# 1. 정류장으로 이동한다.\n");
		
		System.out.println(Transport.Transport(trans));
		
		System.out.printf("어떤 결제수단을 이용하시겠습니까? (1: 카드, 2: 현금, 3: 모바일) : ");
		pay = s.nextInt();
		
		System.out.println(Payment.Payment(pay));
		
		System.out.printf("# 4. 결제를 완료한다.\n");
		
		System.out.println(GetOff.GetOff(trans));
		
		System.out.printf("목적지에 도착했습니다.\n");
	}
}
