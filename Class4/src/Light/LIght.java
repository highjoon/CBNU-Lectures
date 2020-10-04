package Light;

public class LIght {

	public static void main(String[] args) {
		
		// 빛이 1년 동안 가는 거리
		
		long lightspeed;
		long distance;
		
		lightspeed = 300000;
		distance = lightspeed * 3650 * 24 * 60 * 60;
		
		System.out.println("빛이 1년동안 가는 거리 : " + distance + "km.");

	}

}
