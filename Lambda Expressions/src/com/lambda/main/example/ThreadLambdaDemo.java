package com.lambda.main.example;


interface ladma{
	int func();
}

public class ThreadLambdaDemo {

	public static void main(String[] args) {
		Runnable r1 = () -> {
			System.out.print("Inside runnable");
		};
		Thread t1 = new Thread(r1);
		t1.start();
	}

}
