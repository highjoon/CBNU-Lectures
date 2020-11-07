package hw5_1;


// Employee 클래스를 참조하는 Test 클래스 생성.
public class EmployeeTest {
	public static void main(String[] args) {
		
		// 총 3개의 객체 생성.
		// 각 객체에는 한글이름, 영문이름, 사원번호, 부서, 직급의 내용이 포함되어 있음.
		
		// 객체 1.
		Employee employeeLee = new Employee();
		employeeLee.setEmployeeKorName("이순신");
		employeeLee.setEmployeeEngName("Lee, S. S");
		employeeLee.setEmployeeID(1101101);
		employeeLee.setDepartment("경영지원부");
		employeeLee.setEmployeeClass("대리");
		
		// 객체 2.
		Employee employeeKim = new Employee();
		employeeKim.setEmployeeKorName("김유신");
		employeeKim.setEmployeeEngName("Kim, Y. S");
		employeeKim.setEmployeeID(1205631);
		employeeKim.setDepartment("인사부");
		employeeKim.setEmployeeClass("인턴");
		
		// 객체 3.
		Employee employeeHong = new Employee();
		employeeHong.setEmployeeKorName("홍길동");
		employeeHong.setEmployeeEngName("Hong, G. D");
		employeeHong.setEmployeeID(1576364);
		employeeHong.setDepartment("기획부");
		employeeHong.setEmployeeClass("부장");
		
		
		// getter 메소드를 사용하여 각 값들을 불러옴.
		System.out.println("신규 사원증에 포함될 내용 목록입니다.");
		
		System.out.println("========================================");
		
		System.out.println("한 글 이 름 : " + employeeLee.getEmployeeKorName());
		System.out.println("영 문 이 름 : " + employeeLee.getEmployeeEngName());
		System.out.println("사 원 번 호 : " + employeeLee.getEmployeeID());
		System.out.println("부   서   명 : " + employeeLee.getDepartment());
		System.out.println("직         급 : " + employeeLee.getEmployeeClass());
		
		System.out.println("========================================");
		
		System.out.println("한 글 이 름 : " + employeeKim.getEmployeeKorName());
		System.out.println("영 문 이 름 : " + employeeKim.getEmployeeEngName());
		System.out.println("사 원 번 호 : " + employeeKim.getEmployeeID());
		System.out.println("부   서   명 : " + employeeKim.getDepartment());
		System.out.println("직         급 : " + employeeKim.getEmployeeClass());

		System.out.println("========================================");
		
		System.out.println("한 글 이 름 : " + employeeHong.getEmployeeKorName());
		System.out.println("영 문 이 름 : " + employeeHong.getEmployeeEngName());
		System.out.println("사 원 번 호 : " + employeeHong.getEmployeeID());
		System.out.println("부   서   명 : " + employeeHong.getDepartment());
		System.out.println("직         급 : " + employeeHong.getEmployeeClass());
		
		System.out.println("========================================");
		
		System.out.println("이상입니다.");
	}
}