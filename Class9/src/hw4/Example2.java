package hw4;

import java.util.*;

public class Example2 {

	public static void main(String[] args) {
		
		Scanner s = new Scanner(System.in);
		int trans;
		int pay;
		
		System.out.printf("어떤 교통수단을 이용하시겠습니까? (1: 버스, 2: 지하철, 3: 택시) ");
		trans = s.nextInt();
		
		System.out.printf("\n# 1. 정류장으로 이동한다.\n");
		
		switch (trans) {
		
		case 1:
			System.out.printf("# 2. 버스에 탑승한다.\n");
			break;
		case 2:
			System.out.printf("# 2. 지하철에 탑승한다.\n");
			break;
		case 3:
			System.out.printf("# 2. 택시에 탑승한다.\n");
			break;
		default:
			System.out.printf("# 2. 가장 가까운 곳에 있는 교통수단을 사용한다.\n");
			break;
		}
		
		System.out.printf("어떤 결제수단을 이용하시겠습니까? (1: 카드, 2: 현금, 3: 모바일) ");
		pay = s.nextInt();
		
		switch (pay) {
			
		case 1:
			System.out.printf("# 3. 카드로 결제한다.\n");
			break;
		
		case 2:
			System.out.printf("# 3. 현금으로 결제한다.\n");
			break;
		
		case 3:
			System.out.printf("# 3. 모바일로 결제한다.\n");
			break;
			
		default:
			System.out.printf("# 3. 랜덤으로 선택한다.\n");
		}
		
		System.out.printf("# 4. 결제를 완료한다.\n");

		switch (trans) {
				
				case 1:
					System.out.printf("# 5. 버스에서 하차한다.\n");
					break;
				case 2:
					System.out.printf("# 5. 지하철에서 하차한다.\n");
					break;
				case 3:
					System.out.printf("# 5. 택시에서 하차한다.\n");
					break;
				}
		
		System.out.printf("목적지에 도착했습니다.\n");
		
		System.out.printf("어떤 교통수단을 이용하시겠습니까? (1: 버스, 2: 지하철, 3: 택시) ");
		trans = s.nextInt();
		
		System.out.printf("\n# 1. 정류장으로 이동한다.\n");
		
		switch (trans) {
		
		case 1:
			System.out.printf("# 2. 버스에 탑승한다.\n");
			break;
		case 2:
			System.out.printf("# 2. 지하철에 탑승한다.\n");
			break;
		case 3:
			System.out.printf("# 2. 택시에 탑승한다.\n");
			break;
		default:
			System.out.printf("# 2. 가장 가까운 곳에 있는 교통수단을 사용한다.\n");
			break;
		}
		
		System.out.printf("어떤 결제수단을 이용하시겠습니까? (1: 카드, 2: 현금, 3: 모바일) ");
		pay = s.nextInt();
		
		switch (pay) {
			
		case 1:
			System.out.printf("# 3. 카드로 결제한다.\n");
			break;
		
		case 2:
			System.out.printf("# 3. 현금으로 결제한다.\n");
			break;
		
		case 3:
			System.out.printf("# 3. 모바일로 결제한다.\n");
			break;
			
		default:
			System.out.printf("# 3. 랜덤으로 선택한다.\n");
		}
		
		System.out.printf("# 4. 결제를 완료한다.\n");

		switch (trans) {
				
				case 1:
					System.out.printf("# 5. 버스에서 하차한다.\n");
					break;
				case 2:
					System.out.printf("# 5. 지하철에서 하차한다.\n");
					break;
				case 3:
					System.out.printf("# 5. 택시에서 하차한다.\n");
					break;
				}
		
		System.out.printf("목적지에 도착했습니다.\n");
		
		System.out.printf("어떤 교통수단을 이용하시겠습니까? (1: 버스, 2: 지하철, 3: 택시) ");
		trans = s.nextInt();
		
		System.out.printf("\n# 1. 정류장으로 이동한다.\n");
		
		switch (trans) {
		
		case 1:
			System.out.printf("# 2. 버스에 탑승한다.\n");
			break;
		case 2:
			System.out.printf("# 2. 지하철에 탑승한다.\n");
			break;
		case 3:
			System.out.printf("# 2. 택시에 탑승한다.\n");
			break;
		default:
			System.out.printf("# 2. 가장 가까운 곳에 있는 교통수단을 사용한다.\n\n");
			break;
		}
		
		System.out.printf("어떤 결제수단을 이용하시겠습니까? (1: 카드, 2: 현금, 3: 모바일) ");
		pay = s.nextInt();
		
		switch (pay) {
			
		case 1:
			System.out.printf("# 3. 카드로 결제한다.\n");
			break;
		
		case 2:
			System.out.printf("# 3. 현금으로 결제한다.\n");
			break;
		
		case 3:
			System.out.printf("# 3. 모바일로 결제한다.\n");
			break;
			
		default:
			System.out.printf("# 3. 랜덤으로 선택한다.\n");
		}
		
		System.out.printf("# 4. 결제를 완료한다.\n");

		switch (trans) {
				
				case 1:
					System.out.printf("# 5. 버스에서 하차한다.\n");
					break;
				case 2:
					System.out.printf("# 5. 지하철에서 하차한다.\n");
					break;
				case 3:
					System.out.printf("# 5. 택시에서 하차한다.\n");
					break;
				}
		
		System.out.printf("목적지에 도착했습니다.\n\n");

	}
	
}
