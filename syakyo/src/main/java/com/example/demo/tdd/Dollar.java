package com.example.demo.tdd;

public class Dollar extends Money {

  public Dollar(int amount) {
    super(amount);
  }

  public Dollar times(int multipiler) {
    return new Dollar(amount * multipiler);
  }

}
