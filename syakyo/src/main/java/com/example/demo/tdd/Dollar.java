package com.example.demo.tdd;

public class Dollar {
  public int amount;

  public Dollar(int amount) {
    this.amount = amount;
  }

  public Dollar times(int multipiler) {
    return new Dollar( amount * multipiler);
  }
}
