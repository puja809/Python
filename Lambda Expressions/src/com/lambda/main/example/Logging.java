package com.lambda.main.example;

import java.io.IOException;
import java.util.logging.FileHandler;
import java.util.logging.Logger;
import java.util.logging.SimpleFormatter;

public class Logging {
	static Logger log = Logger.getLogger("Logging.class");
	static FileHandler fh = null;
	static SimpleFormatter formatter; 
	
	static {
		try {
			fh = new FileHandler("test.log");
			formatter = new SimpleFormatter();
			fh.setFormatter(formatter);
			log.addHandler(fh);
		} catch (SecurityException | IOException e) {
			e.printStackTrace();
		}
	}
	
	public void show() {
		log.info("inside non static show");
	}
	
	public static void statShow() {
		log.info("inside static show");
	}
	
	public static void main(String[] args) {
		Logging ll = new Logging();
		ll.show();
//		statShow();
	}
}
