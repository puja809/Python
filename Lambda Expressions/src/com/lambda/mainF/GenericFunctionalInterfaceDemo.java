package com.lambda.mainF;

/**
 * 
 * @author nikhil
 * The objective of this example is to how a lambda expression is created and called
 * and how we can pass function as an argument, which is a feature of functional programming
 * We'll see how we can use a boolean abstract type with Lambda Expressions and test it
 * We have 2 examples here for performing similar task 
 * 1. By passing as an argument
 * 2. By directly using it.
 * We'll be using generics for the use
 */
//It is a functional interface as it has only one abstract method
interface SomeFunc<T>{
	T func(T n);
}

public class GenericFunctionalInterfaceDemo {
		
	public static void main(String args[]) {
		
		// By defining as string type
		SomeFunc<String> myNum1 = (str)-> {
			int i;
			String result="";
			for(i=str.length()-1;i>=0;i--) {
				result+=str.charAt(i);
			}
			return result;
		};
		
		System.out.println("Lambda reversed is "+myNum1.func("Lambda"));
		
		// By defining as integer type
		SomeFunc<Integer> myNum2= (n)-> {
			int result=1;
			for(int i=1;i<=n;i++)
				result=i*result;
			return result;
		};
		
		System.out.println("Factorial of a number is "+myNum2.func(5));
	}
}

