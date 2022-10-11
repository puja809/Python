package com.lambda.main.example;

public class Bike {
	public String name;
	public int rank;
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public int getRank() {
		return rank;
	}
	public void setRank(int rank) {
		this.rank = rank;
	}
	public Bike(String name, int rank) {
		super();
		this.name = name;
		this.rank = rank;
	}
	@Override
	public String toString() {
		return "Bike [name=" + name + ", rank=" + rank + "]";
	}
	
}
