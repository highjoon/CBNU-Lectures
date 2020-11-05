package hw5_2;

import java.text.DecimalFormat;
import java.util.Scanner;


class Customer {
	
	private String CustomerName;
	private String CustomerGrade;
	private int CustomerID;
	private long totalSale;
	private int bonus;
	private double bonusRatio;
	
	public void addSale(long price) {
		this.totalSale += price;
	}
	
	public void gradeSet() {
		if (totalSale > 100000) {
			CustomerGrade = "GOLD";
		} else {
			CustomerGrade = "SILVER";
		}
	}
	
	public void bonusSale() {
		if (CustomerGrade == "GOLD") {
			bonusRatio = 0.2	;
			bonus = (int) (totalSale * bonusRatio);
		} else {
			bonusRatio = 0.01;
			bonus = (int) (totalSale * bonusRatio);
		}
	}
	
	public String showCustomerInfo() {
		DecimalFormat formatter = new DecimalFormat("###,###");
		return CustomerName + "님의 회원번호는 " + CustomerID + "이고, " + "회원 등급은 " + CustomerGrade + "이며, " + "총 결제금액은 보너스 " + formatter.format(bonus)+ "원을 차감한 " + formatter.format(totalSale-bonus) + "원 입니다." ;
	}

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
