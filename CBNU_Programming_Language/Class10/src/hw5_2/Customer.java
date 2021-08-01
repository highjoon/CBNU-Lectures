package hw5_2;

// 총 결제금액의 세자릿수마다 , 표시를 하기 위한 기능 선언.
import java.text.DecimalFormat;
import java.util.Scanner;


class Customer {
	
	// 회원이름, 회원등급, 회원번호, 총결제금액, 보너스 금액, 보너스 할인율 이상 6개의 private 변수를 선언함.
	private String CustomerName;
	private String CustomerGrade;
	private int CustomerID;
	private long totalSale;
	private int bonus;
	private double bonusRatio;
	
	// 총 결제금액을 계산하는 addSale 메소드.
	public void addSale(long price) {
		this.totalSale += price;
	}
	
	// 총 결제금액에 따라 회원 등급을 결정하는 gradeSet 메소드.
	// 10000원 미만 : BRONZE 등급.
	// 10000원 이상 50000원 이하 : SILVER 등급.
	// 100000원 이상 : GOLD 등급.
	public void gradeSet() {
		if (totalSale >= 100000) {
			CustomerGrade = "GOLD";
		} else if (totalSale >= 50000){
			CustomerGrade = "SILVER";
		} else if (totalSale < 10000) {
			CustomerGrade = "BRONZE";
		}
	}
	
	// 회원 등급에 따라 보너스 할인율을 결정하는 bonusSale 메소드.
	// BRONZE 등급은 할인율 없음.
	// SILVER 등급은 0.01%의 할인율 적용.
	// GOLD 등급은 0.2%의 할인율 적용.
	public void bonusSale() {
		if (CustomerGrade == "GOLD") {
			bonusRatio = 0.2	;
			bonus = (int) (totalSale * bonusRatio);
		} else if (CustomerGrade == "SILVER"){
			bonusRatio = 0.01;
			bonus = (int) (totalSale * bonusRatio);
		}
	}
	
	// 모든 정보를 프린트하는 showCustomerInfo 메소드.
	public String showCustomerInfo() {
		DecimalFormat formatter = new DecimalFormat("###,###");
		return CustomerName + "님의 회원번호는 " + CustomerID + "이고, " + "회원 등급은 " + CustomerGrade + "이며, " 
				+ "총 결제금액은 보너스 " + formatter.format(bonus)+ "원을 차감한 " + formatter.format(totalSale-bonus) + "원 입니다." ;
	}
	
	// 이하 getter, setter 메소드.
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
