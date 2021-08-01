package array;
public class GetMin {

	public static void main(String[] args) {
		int  prices [] = {120, 30, 190, 60, 180, 80, 120, 40, 10, 190};
		int minimum = prices[0];
		
		for (int i = 1; i < prices.length; i++) {
			if (prices[i] < minimum) {
				minimum = prices[i];
			}
		}
		
		System.out.print("ÃÖ¼Ú°ª : " + minimum);
	}

}
