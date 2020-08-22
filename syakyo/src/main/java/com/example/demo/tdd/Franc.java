package com.example.demo.tdd;

public class Franc {
  private int amount;

  public Franc(int amount) {
    this.amount = amount;
  }

  public Franc times(int multipiler) {
    return new Franc(amount * multipiler);
  }

  public boolean equals(Object object) {
    Franc dollar = (Franc) object;
    return amount == dollar.amount;
  }
}
