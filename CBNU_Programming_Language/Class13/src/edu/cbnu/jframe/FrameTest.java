package edu.cbnu.jframe;

import javax.swing.*;																							// ���� Ŭ�������� javax.swing ��Ű�� �ȿ� �������.

public class FrameTest {

	public static void main(String[] args) {
		
		JFrame f = new JFrame("Frame Test");												// new  ������ �̿��Ͽ� JFrame ��ü ����.
																																// ������ f�� ������ ��ü�� �ǹ���.
		f.setSize(300, 200);																					// setSize ȣ�� ==> ������ ũ�� ����.
		f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);					// Close ��ư�� ������ ��ü ���α׷� ����.
		f.setVisible(true);																						// �������� ȭ�鿡 ��Ÿ���� ��.
	}

}
