package com.example.demo.tdd;

public abstract class Money {
  protected int amount;

  public static Money franc(int amount) {
    return new Franc(amount);
  }

  abstract Money times(int multiplier);

  public Money(int amount) {
    this.amount = amount;
  }

  public static Money dollar(int amount) {
    return new Dollar(amount);
  }


  public boolean equals(Object object) {
    Money money = (Money) object;
    return amount == money.amount
        && getClass().equals(money.getClass());
  }
}
