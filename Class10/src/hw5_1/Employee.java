package hw5_1;

class Employee {
	
	private String employeeKorName;
	private String employeeEngName;
	private int employeeID;
	private String Department;
	private String employeeClass;
	
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
}