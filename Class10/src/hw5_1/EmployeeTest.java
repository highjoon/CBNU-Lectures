package hw5_1;

public class EmployeeTest {
	public static void main(String[] args) {
		
		Employee employeeLee = new Employee();
		employeeLee.setEmployeeKorName("이순신");
		employeeLee.setEmployeeEngName("Lee, S. S");
		employeeLee.setEmployeeID(1101101);
		employeeLee.setDepartment("경영지원부");
		employeeLee.setEmployeeClass("대리");
		
		Employee employeeKim = new Employee();
		employeeKim.setEmployeeKorName("김유신");
		employeeKim.setEmployeeEngName("Kim, Y. S");
		employeeKim.setEmployeeID(1205631);
		employeeKim.setDepartment("인사부");
		employeeKim.setEmployeeClass("인턴");
		
		Employee employeeHong = new Employee();
		employeeHong.setEmployeeKorName("홍길동");
		employeeHong.setEmployeeEngName("Hong, G. D");
		employeeHong.setEmployeeID(1576364);
		employeeHong.setDepartment("기획부");
		employeeHong.setEmployeeClass("부장");
		
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