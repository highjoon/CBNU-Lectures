package hw5_1;

class Employee {
	
	// 모든 필드에 private을 붙임으로써 접근제어 설정.
	// 간접적인 필드 접근 방식을 사용하여 모든 필드에 접근자 (Getter) 와 설정자 (Setter) 생성.
	// 설정자 (Setter)에서 this를 사용함으로써 변수에 접근.
	
	private String employeeKorName;
	private String employeeEngName;
	private int employeeID;
	private String Department;
	private String employeeClass;
	private int score;
	
	// 모든 외부 클래스에서 접근 가능한 메소드 추가.
	// 승진 점수 추가 또는 삭감.
	
	public void AddScroe(int value) {
		score += value;
	}
	
	public void SubScore(int value) {
		score -= value;
	}
	
	
	public String getEmployeeKorName() {
		return employeeKorName;
	}
	
	public void setEmployeeKorName(String employeeKorName) {
		this.employeeKorName = employeeKorName;
	}
	
	public String getEmployeeEngName() {
		return employeeEngName;
	}
	
	public void setEmployeeEngName(String employeeEngName) {
		this.employeeEngName = employeeEngName;
	}
	
	public int getEmployeeID() {
		return employeeID;
	}
	
	public void setEmployeeID(int employeeID) {
		this.employeeID = employeeID;
	}
	
	public String getDepartment() {
		return Department;
	}
	
	public void setDepartment(String department) {
		Department = department;
	}
	
	public String getEmployeeClass() {
		return employeeClass;
	}
	
	public void setEmployeeClass(String employeeClass) {
		this.employeeClass = employeeClass;
	}


	public int getScore() {
		return score;
	}


	public void setScore(int score) {
		this.score = score;
	}
}