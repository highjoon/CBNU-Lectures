package method;

public class Ex09_16 {
	
	static void func1() {
		System.out.printf("void �� �޼ҵ�� �����ٰ� ����.\n");
//		void���� �޼ҵ�� ��ȯ ���� ����.
	}
	
	static int func2() {
		return 100;
//		static int �� �޼ҵ�ν� return ���� ��ȯ�Ѵ�. ���⼭�� 100�� ��ȯ�ȴ�.
	}
	
	public static void main(String args[]) {
		
		int a;
		
		func1(); 		// void �� �޼ҵ带 ȣ���Ѵ�.
		
		a = func2();
		System.out.printf("int �� �޼ҵ忡�� ������ �� ==> %d\n", a);		// int �� �޼ҵ带 ȣ���Ѵ�.
	}

}
