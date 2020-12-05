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
		System.out.printf("100과 200의 plus() 메소드 결과는 :  %d\n", hap);
		
		hap = plus(1000000000, 2000000000);
		System.out.printf("1000000000과 2000000000의 plus() 메소드 결과는 : %d\n", hap);
		
		// 자바에서 제공하는 Math API 활용.
		int mathAPI;
		mathAPI = Math.addExact(100,  200);
		System.out.printf("100과 200의 addExact() 메소드 결과는 : %d\n", mathAPI);
		
		mathAPI = Math.addExact(1000000000,  2000000000);
		System.out.printf("1000000000과 2000000000의 addExact() 메소드 결과는 : %d\n", mathAPI);
	}
}
