package method;

public class Ex09_13 {
	
	static int plus(int v1, int v2) {
		int result;
		result = v1 + v2;
		return result;
	}
	
	public static void main(String args[]) {
		int hap;
		hap = plus(100, 200);
		
		System.out.printf("100�� 200�� puls() �޼ҵ� ����� : %d\n", hap);
	}

}