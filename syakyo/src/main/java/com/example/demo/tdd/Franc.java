package com.example.demo.tdd;

public class Franc extends Money {
  public Franc(int amount) {
    super(amount, "CHF");
  }

  public Money times(int multipiler) {
    return Money.franc(amount * multipiler);
  }

}
