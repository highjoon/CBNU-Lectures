package hw5_1;


// Employee Ŭ������ �����ϴ� Test Ŭ���� ����.
public class EmployeeTest {
	public static void main(String[] args) {
		
		// �� 3���� ��ü ����.
		// �� ��ü���� �ѱ��̸�, �����̸�, �����ȣ, �μ�, ����, ���������� ������ ���ԵǾ� ����.
		
		// ��ü 1.
		Employee employeeLee = new Employee();
		employeeLee.setEmployeeKorName("�̼���");
		employeeLee.setEmployeeEngName("Lee, S. S");
		employeeLee.setEmployeeID(1101101);
		employeeLee.setDepartment("�濵������");
		employeeLee.setEmployeeClass("�븮");
		employeeLee.AddScroe(90);
		employeeLee.SubScore(5);
		
		// ��ü 2.
		Employee employeeKim = new Employee();
		employeeKim.setEmployeeKorName("������");
		employeeKim.setEmployeeEngName("Kim, Y. S");
		employeeKim.setEmployeeID(1205631);
		employeeKim.setDepartment("�λ��");
		employeeKim.setEmployeeClass("�븮");
		employeeKim.AddScroe(91);
		
		// ��ü 3.
		Employee employeeHong = new Employee();
		employeeHong.setEmployeeKorName("ȫ�浿");
		employeeHong.setEmployeeEngName("Hong, G. D");
		employeeHong.setEmployeeID(1576364);
		employeeHong.setDepartment("��ȹ��");
		employeeHong.setEmployeeClass("�븮");
		employeeHong.AddScroe(97);
		employeeHong.SubScore(2);
		
		
		// getter �޼ҵ带 ����Ͽ� �� ������ �ҷ���.
		System.out.println("4/4 �б� �����ӿ� ���� �ĺ� ����Դϴ�.");
		
		System.out.println("========================================");
		
		System.out.println("�� �� �� �� : " + employeeLee.getEmployeeKorName());
		System.out.println("�� �� �� �� : " + employeeLee.getEmployeeEngName());
		System.out.println("�� �� �� ȣ : " + employeeLee.getEmployeeID());
		System.out.println("��   ��   �� : " + employeeLee.getDepartment());
		System.out.println("��         �� : " + employeeLee.getEmployeeClass());
		System.out.println("�� �� �� �� : " + employeeLee.getScore());
		
		System.out.println("========================================");
		
		System.out.println("�� �� �� �� : " + employeeKim.getEmployeeKorName());
		System.out.println("�� �� �� �� : " + employeeKim.getEmployeeEngName());
		System.out.println("�� �� �� ȣ : " + employeeKim.getEmployeeID());
		System.out.println("��   ��   �� : " + employeeKim.getDepartment());
		System.out.println("��         �� : " + employeeKim.getEmployeeClass());
		System.out.println("�� �� �� �� : " + employeeKim.getScore());

		System.out.println("========================================");
		
		System.out.println("�� �� �� �� : " + employeeHong.getEmployeeKorName());
		System.out.println("�� �� �� �� : " + employeeHong.getEmployeeEngName());
		System.out.println("�� �� �� ȣ : " + employeeHong.getEmployeeID());
		System.out.println("��   ��   �� : " + employeeHong.getDepartment());
		System.out.println("��         �� : " + employeeHong.getEmployeeClass());
		System.out.println("�� �� �� �� : " + employeeHong.getScore());
		
		System.out.println("========================================");
		
		System.out.println("�̻��Դϴ�.");
	}
}