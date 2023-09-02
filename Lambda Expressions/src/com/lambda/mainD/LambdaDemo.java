package com.lambda.mainD;

/**
 * 
 * @author nikhil
 * The objective of this example is to how a lambda expression is created and called
 * and how we can pass function as an argument, which is a feature of functional programming
 * We'll see how we can use a boolean abstract type with Lambda Expressions and test it
 * We have 2 examples here for performing similar task 
 * 1. By passing as an argument
 * 2. By directly using it.
 * Here we'll be having 2 parameters lambda function
 */
//It is a functional interface as it has only one abstract method
interface MyNumber{
	boolean getValue(int m,int n);
}

public class LambdaDemo {
	
	public static boolean perform(MyNumber num,int m,int n) {
		return num.getValue(m,n);
	}
	
	public static void main(String args[]) {
		// we have defined declared a variable of type MyNumber
		// In this example we are passing a function as an argument and performing the required task
		MyNumber myNum1;
		myNum1 = (m,n)-> m<n; // Defining a lambda function to check even number. 
		System.out.println("The number 5 is less than 6 "+perform(myNum1,5,6));		
		System.out.println("The number 6 is less than 5 "+perform(myNum1,6,5));
		
		
		// In this example we are defining the value and performing the task accordingly
		System.out.println("The number 5 is less than 6 "+myNum1.getValue(5,6));		
		System.out.println("The number 6 is less than 5 "+myNum1.getValue(6,5));
	}
}
