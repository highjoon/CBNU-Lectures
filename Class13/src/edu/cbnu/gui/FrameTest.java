package edu.cbnu.gui;

import javax.swing.*;																							// 스윙 클래스들은 javax.swing 패키지 안에 들어있음.

public class FrameTest {

	public static void main(String[] args) {
		
		JFrame f = new JFrame("Frame Test");												// new  연산자 이용하여 JFrame 객체 생성.
																																// 참조된 f가 생성된 객체를 의미함.
		f.setSize(300, 200);																					// setSize 호출 ==> 프레임 크기 설정.
		f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);					// Close 버튼을 누르면 전체 프로그램 종료.
		f.setVisible(true);																						// 프레임을 화면에 나타나게 함.
	}

}
