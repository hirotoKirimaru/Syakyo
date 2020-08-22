package com.example.demo.tdd;

public class Dollar extends Money {
  public Dollar(int amount) {
    super(amount, "USD");
  }

  public Money times(int multipiler) {
    return Money.dollar(amount * multipiler);
  }

}
