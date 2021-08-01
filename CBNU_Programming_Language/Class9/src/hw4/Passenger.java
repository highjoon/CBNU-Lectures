package hw4;

// main 메소드를 사용하여 객체지향 형식으로 변환.
// Passenger 클래스. (Main() 메소드)
// GetOff 클래스. (교통수단 하차 메소드)
// Payment 클래스. (결제수단 선택 메소드)
// Transport 클래스. (교통수단 선택 메소드)
// 총 4개의 클래스로 분할하여 작성.
// main() 메소드가 있는 Passenger 클래스에서 나머지 3개의 클래스를 참조하여 실행.

import java.util.*;

// Passenger 클래스

public class Passenger {

	public static void main(String[] args) {
		
		// main 메소드
		
		Scanner s = new Scanner(System.in);
		int trans;
		int pay;
		
		System.out.printf("어떤 교통수단을 이용하시겠습니까? (1: 버스, 2: 지하철, 3: 택시) : ");
		trans = s.nextInt();
		
		System.out.printf("\n# 1. 정류장으로 이동한다.\n");
		
		// Transport 클래스의 Transport 메소드 참조.
		System.out.println(Transport.Transport(trans));
		
		System.out.printf("어떤 결제수단을 이용하시겠습니까? (1: 카드, 2: 현금, 3: 모바일) : ");
		pay = s.nextInt();
		
		// Payment 클래스의 Payment 메소드 참조.
		System.out.println(Payment.Payment(pay));
		
		System.out.printf("# 4. 결제를 완료한다.\n");
		
		// GetOff 클래스의 GetOff 메소드 참조.
		System.out.println(GetOff.GetOff(trans));
		
		System.out.printf("목적지에 도착했습니다.\n");
	}
}
