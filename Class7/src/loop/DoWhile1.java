package loop;

public class DoWhile1 {

	public static void main(String[] args) {
		int i = 10;
		
		do {
			System.out.println("i의 값 : " + i);
			i++;
		}
		
		while (i < 3);
		
//		조건 자체는 맞지 않지만 do while문 이므로, 반복문이 한차례 먼저 실행 된 후 조건의 참/거짓 여부를 판단한다.
//		따라서 i = 10 이 먼저 실행된 후 break 한다.

	}

}
