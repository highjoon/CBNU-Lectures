package edu.cbnu.debuging;

public class Method {
	
	static int plus (int v1, int v2) {
		int result;
		result = v1 + v2;
		return result;
	}

	public static void main(String[] args) {
		int hap;
		hap = plus(100, 200);
		System.out.printf("100�� 200�� plus() �޼ҵ� ����� :  %d\n", hap);
		
		hap = plus(1000000000, 2000000000);
		System.out.printf("1000000000�� 2000000000�� plus() �޼ҵ� ����� : %d\n", hap);
		
		// �ڹٿ��� �����ϴ� Math API Ȱ��.
		int mathAPI;
		mathAPI = Math.addExact(100,  200);
		System.out.printf("100�� 200�� addExact() �޼ҵ� ����� : %d\n", mathAPI);
		
		mathAPI = Math.addExact(1000000000,  2000000000);
		System.out.printf("1000000000�� 2000000000�� addExact() �޼ҵ� ����� : %d\n", mathAPI);
	}
}
