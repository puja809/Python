package com.lambda.mainE;
/**
 * 
 * @author nikhil
 * The objective of this example is to how a block body lambda expression is created and called
 * and how we can pass function as an argument, which is a feature of functional programming
 * We'll see how we can use a boolean abstract type with Lambda Expressions and test it
 * We have 2 examples here for performing similar task 
 * 1. By passing as an argument
 * 2. By directly using it.
 * Here we'll try to find the factorial of a number and print it in lambda itself
 */
//It is a functional interface as it has only one abstract method
interface MyNumber{
	void getValue(int n);
}

public class LambdaDemo {
	
	public static void perform(MyNumber num,int n) {
		num.getValue(5);
	}
	
	public static void main(String args[]) {
		// we have defined declared a variable of type MyNumber
		// In this example we are passing a function as an argument and performing the required task
		MyNumber myNum1;
		myNum1 = (n)-> {
			System.out.println("The factorial of the number "+n+" are");
			for(int i=1;i<=n;i++) {
				if(n%i==0)
					System.out.print(i+"\t");
			}
			System.out.println();
		}; // print the factorial of a number 
		System.out.println("By passing lambda expression as a parameter");
		perform(myNum1,5);
		
		System.out.println("By using the function directly");
		myNum1.getValue(6);
	}
}
