package com.example.demo.tdd;

public abstract class Money {
  protected int amount;
  protected String currency;

  public Money(int amount, String currency) {
    this.amount = amount;
    this.currency = currency;

  }

  abstract Money times(int multiplier);
  public String currency(){
    return currency;
  }


  public static Money dollar(int amount) {
    return new Dollar(amount);
  }

  public static Money franc(int amount) {
    return new Franc(amount);
  }

  public boolean equals(Object object) {
    Money money = (Money) object;
    return amount == money.amount
        && getClass().equals(money.getClass());
  }
}
