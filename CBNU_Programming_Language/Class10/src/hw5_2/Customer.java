package hw5_2;

// �� �����ݾ��� ���ڸ������� , ǥ�ø� �ϱ� ���� ��� ����.
import java.text.DecimalFormat;
import java.util.Scanner;


class Customer {
	
	// ȸ���̸�, ȸ�����, ȸ����ȣ, �Ѱ����ݾ�, ���ʽ� �ݾ�, ���ʽ� ������ �̻� 6���� private ������ ������.
	private String CustomerName;
	private String CustomerGrade;
	private int CustomerID;
	private long totalSale;
	private int bonus;
	private double bonusRatio;
	
	// �� �����ݾ��� ����ϴ� addSale �޼ҵ�.
	public void addSale(long price) {
		this.totalSale += price;
	}
	
	// �� �����ݾ׿� ���� ȸ�� ����� �����ϴ� gradeSet �޼ҵ�.
	// 10000�� �̸� : BRONZE ���.
	// 10000�� �̻� 50000�� ���� : SILVER ���.
	// 100000�� �̻� : GOLD ���.
	public void gradeSet() {
		if (totalSale >= 100000) {
			CustomerGrade = "GOLD";
		} else if (totalSale >= 50000){
			CustomerGrade = "SILVER";
		} else if (totalSale < 10000) {
			CustomerGrade = "BRONZE";
		}
	}
	
	// ȸ�� ��޿� ���� ���ʽ� �������� �����ϴ� bonusSale �޼ҵ�.
	// BRONZE ����� ������ ����.
	// SILVER ����� 0.01%�� ������ ����.
	// GOLD ����� 0.2%�� ������ ����.
	public void bonusSale() {
		if (CustomerGrade == "GOLD") {
			bonusRatio = 0.2	;
			bonus = (int) (totalSale * bonusRatio);
		} else if (CustomerGrade == "SILVER"){
			bonusRatio = 0.01;
			bonus = (int) (totalSale * bonusRatio);
		}
	}
	
	// ��� ������ ����Ʈ�ϴ� showCustomerInfo �޼ҵ�.
	public String showCustomerInfo() {
		DecimalFormat formatter = new DecimalFormat("###,###");
		return CustomerName + "���� ȸ����ȣ�� " + CustomerID + "�̰�, " + "ȸ�� ����� " + CustomerGrade + "�̸�, " 
				+ "�� �����ݾ��� ���ʽ� " + formatter.format(bonus)+ "���� ������ " + formatter.format(totalSale-bonus) + "�� �Դϴ�." ;
	}
	
	// ���� getter, setter �޼ҵ�.
	public String getCustomerName() {
		return CustomerName;
	}

	public void setCustomerName(String customerName) {
		CustomerName = customerName;
	}

	public String getCustomerGrade() {
		return CustomerGrade;
	}

	public void setCustomerGrade(String customerGrade) {
		CustomerGrade = customerGrade;
	}

	public int getCustomerID() {
		return CustomerID;
	}

	public void setCustomerID(int customerID) {
		CustomerID = customerID;
	}

	public long getTotalSale() {
		return totalSale;
	}

	public void setTotalSale(long totalSale) {
		this.totalSale = totalSale;
	}

	public int getBonus() {
		return bonus;
	}

	public void setBonus(int bonus) {
		this.bonus = bonus;
	}

	public double getBonusRatio() {
		return bonusRatio;
	}

	public void setBonusRatio(double bonusRatio) {
		this.bonusRatio = bonusRatio;
	}



}
