package edu.cbnu.Mylab;

import javax.swing.*;

public class Mylab {

	public static void main(String[] args) {
		JFrame f = new JFrame();																// �Ѱ��� ������ �ʿ� ==> �������� ������ ��Ÿ���� Ŭ���� JFrame ��ü�� �ϳ� ����. 
		JPanel panel = new JPanel();															// �г��� �����ӿ� �߰� ==> �г��� �����ϰ� �����ӿ� �߰�.
		f.add(panel);
		
		JLabel label1 = new JLabel("ȭ�� �µ�");										// �ʿ��� ������Ʈ���� �����ϰ� �гο� �߰�.
		JLabel label2 = new JLabel("���� �µ�");
		JTextField field1 = new JTextField(15);
		JTextField field2 = new JTextField(15);
		JButton button = new JButton("��ȯ");
		
		panel.add(label1);
		panel.add(field1);
		panel.add(label2);
		panel.add(field2);
		panel.add(button);
		
		f.setSize(300, 150);																			// �������� �Ӽ��� ����.
		f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		f.setTitle("�µ���ȯ��");
		f.setVisible(true);
	}

}
