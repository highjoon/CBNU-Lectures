package edu.cbnu.api;

import java.util.Date;
import java.util.Calendar;
import java.util.GregorianCalendar;

public class CurrentTime {
	public static void main(String[] args) {
		
		Date currentTime = new Date();
		System.out.println(currentTime);
		
		Calendar currentCalendar = new GregorianCalendar();
		currentCalendar.setTime(currentTime);
		System.out.println(currentCalendar.get(Calendar.YEAR) + "�� " + 
				(currentCalendar.get(Calendar.MONTH)+ 1) + "�� " +
				currentCalendar.get(Calendar.DAY_OF_MONTH) + "�� " +
				currentCalendar.get(Calendar.HOUR_OF_DAY) + "�� " +
				currentCalendar.get(Calendar.MINUTE) + "�� " +
				currentCalendar.get(Calendar.SECOND) + "��"
				);
	}

}