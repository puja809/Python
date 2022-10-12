package com.lambda.mainG;


interface DoubleNumericArrayFunc{
	double func(double[] n) throws EmptyArrayException;
}
class EmptyArrayException extends Exception{
	EmptyArrayException(){
		super("Array Empty");
	}
}
public class LambdaExceptionDemo {
	public static void main(String args[]) throws EmptyArrayException{		
		DoubleNumericArrayFunc average = (n)->{
			double result = 0.0d;
			if(n.length==0) {
				throw new EmptyArrayException();
			}
			else {
				for(double d:n) {
					result+=d;
				}
			}
			return result/n.length;
		};
		double[] values1 = {1.0,2.0,3.0,4.0};
		double[] values2 = {};
		
		System.out.println("The aveage is "+average.func(values1));
		System.out.println("The aveage is "+average.func(values2));
	}
}
