package com.lambda.mainC;

/**
 * 
 * @author nikhil
 * The objective of this example is to how a lambda expression is created and called
 * and how we can pass function as an argument, which is a feature of functional programming
 * We'll see how we can use a boolean abstract type with Lambda Expressions and test it
 * We have 2 examples here for performing similar task 
 * 1. By passing as an argument
 * 2. By directly using it.
 *  
 */
//It is a functional interface as it has only one abstract method
interface MyNumber{
	boolean getValue(int n);
}

public class LambdaDemo {
	
	public static boolean perform(MyNumber num,int n) {
		return num.getValue(n);
	}
	
	public static void main(String args[]) {
		// we have defined declared a variable of type MyNumber
		// In this example we are passing a function as an argument and performing the required task
		MyNumber myNum1;
		myNum1 = (n)-> n%2==0; // Defining a lambda function to check even number. 
		System.out.println("The number 5 is even "+perform(myNum1,5));		
		System.out.println("The number 6 is even "+perform(myNum1,6));
		
		
		// In this example we are defining the value and performing the task accordingly
		MyNumber myNum2;
		myNum2 = (n)-> n%2!=0; // Defining a lambda function to check odd number. 
		System.out.println("The number 5 is odd "+myNum2.getValue(5));		
		System.out.println("The number 6 is odd "+myNum2.getValue(6));
	}
}
