package edu.cbnu.multiple_inheritance;

 interface Car {																		// Car �������̽� ����.
	 abstract void work();														// ��� �߻� �޼ҵ��̹Ƿ� abstract�� ���� ����.
}
 
 interface Cannon {																// Cannon �������̽� ����.
	 void fire();																			// abstract ����.
 }

 class Tank implements Car, Cannon {								// implement�� ���. (Car�� Cannon �������̽��� ���߻������ ����)
	 public void work() {																// interface�� �߻�޼ҵ带 �ϼ��Ҷ��� public Ű���带 ����.
		 System.out.println("��ũ�� �����մϴ�.");
	 }
	 
	 public void fire() {																// �������̵�.
		 System.out.println("��ũ�� ���� �߻��մϴ�.");
	 }
 }