package edu.cbnu.MyFrame;

import javax.swing.JFrame;

public class MyFrame extends JFrame {												// JFrame�� ����Ͽ� MyFrame ����.
	public MyFrame() {
		setSize(300, 200);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setTitle("MyFrame");
		setVisible(true);
	}
	
	public static void main (String [] args) {											// MyFrame�� ��ü ���� ==> ������ ȣ��.
		MyFrame f = new MyFrame();
	}
}
