package method;

public class Test {

	public static void main(String[] args) {
		
		int sum = 0;
		int result = 0;
		
		
	}
	
	public int sum (int i, int j) {
		int r = 0;
		for (int h = i; h <= j; h++) {
			r += h;
		}
		
		return r;
	}
	
	public String evenOdd (int sum) {
		String r = new String();
		if ((sum % 2) == 0) {
			r = "Â¦¼ö ÀÔ´Ï´Ù.";
		} else {
			r = "È¦¼ö ÀÔ´Ï´Ù.";
		}
		return r;
	}

}
