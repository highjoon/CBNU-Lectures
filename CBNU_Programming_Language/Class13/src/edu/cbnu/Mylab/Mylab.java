package edu.cbnu.Mylab;

import javax.swing.*;

public class Mylab {

	public static void main(String[] args) {
		JFrame f = new JFrame();																// 한개의 윈도우 필요 ==> 스윙에서 윈도를 나타내는 클래스 JFrame 객체를 하나 생성. 
		JPanel panel = new JPanel();															// 패널을 프레임에 추가 ==> 패널을 생성하고 프레임에 추가.
		f.add(panel);
		
		JLabel label1 = new JLabel("화씨 온도");										// 필요한 컴포넌트들을 생성하고 패널에 추가.
		JLabel label2 = new JLabel("섭씨 온도");
		JTextField field1 = new JTextField(15);
		JTextField field2 = new JTextField(15);
		JButton button = new JButton("변환");
		
		panel.add(label1);
		panel.add(field1);
		panel.add(label2);
		panel.add(field2);
		panel.add(button);
		
		f.setSize(300, 150);																			// 프레임의 속성을 변경.
		f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		f.setTitle("온도변환기");
		f.setVisible(true);
	}

}
