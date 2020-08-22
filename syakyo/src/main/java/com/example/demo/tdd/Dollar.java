package com.example.demo.tdd;

public class Dollar extends Money {

  public Dollar(int amount) {
    super(amount);
  }

  public Money times(int multipiler) {
    return new Dollar(amount * multipiler);
  }

}
