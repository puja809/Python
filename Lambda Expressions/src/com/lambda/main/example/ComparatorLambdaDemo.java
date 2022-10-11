package com.lambda.main.example;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class ComparatorLambdaDemo {
	
	public static List<Bike> getListOfBikes(){
		List<Bike> bikes = new ArrayList<>();
		bikes.add(new Bike("simple",1));
		bikes.add(new Bike("ola",6));
		bikes.add(new Bike("bajaj",5));
		bikes.add(new Bike("ather",4));
		bikes.add(new Bike("okinava",3));
		bikes.add(new Bike("tork",2));
		return bikes;
	}
	
	public static void main(String[] args) {
		List<Bike> bikes = getListOfBikes();
		Collections.sort(bikes, ((o1,o2)->(o1.getRank()<o2.getRank())?-1:(o1.getRank()>o2.getRank())?1:0));
	}
	
}
