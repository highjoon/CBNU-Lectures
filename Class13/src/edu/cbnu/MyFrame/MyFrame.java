package edu.cbnu.MyFrame;

import javax.swing.JFrame;

public class MyFrame extends JFrame {												// JFrame을 상속하여 MyFrame 정의.
	public MyFrame() {
		setSize(300, 200);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setTitle("MyFrame");
		setVisible(true);
	}
	
	public static void main (String [] args) {											// MyFrame의 객체 생성 ==> 생성자 호출.
		MyFrame f = new MyFrame();
	}
}
