package method;

public class Ex09_16 {
	
	static void func1() {
		System.out.printf("void 형 메소드는 돌려줄게 없음.\n");
//		void형의 메소드는 반환 값이 없다.
	}
	
	static int func2() {
		return 100;
//		static int 형 메소드로써 return 값을 반환한다. 여기서는 100이 반환된다.
	}
	
	public static void main(String args[]) {
		
		int a;
		
		func1(); 		// void 형 메소드를 호출한다.
		
		a = func2();
		System.out.printf("int 형 메소드에서 돌려준 값 ==> %d\n", a);		// int 형 메소드를 호출한다.
	}

}
