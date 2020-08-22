package com.example.demo.tdd;

public class Franc extends Money {

  public Franc(int amount) {
    super(amount);
  }

  public Franc times(int multipiler) {
    return new Franc(amount * multipiler);
  }

}
