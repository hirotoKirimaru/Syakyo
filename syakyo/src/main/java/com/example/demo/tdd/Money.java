package com.example.demo.tdd;

public class Money implements Expression {
  protected int amount;
  protected String currency;

  public Money(int amount, String currency) {
    this.amount = amount;
    this.currency = currency;
  }

  public Expression times(int multipiler) {
    return new Money(amount * multipiler, currency);
  }

  public String currency() {
    return currency;
  }


  public static Money dollar(int amount) {
    return new Money(amount, "USD");
  }

  public static Money franc(int amount) {
    return new Money(amount, "CHF");
  }

  public boolean equals(Object object) {
    Money money = (Money) object;
    return amount == money.amount
        && currency().equals(money.currency());
  }

  public String toString() {
    return amount + " " + currency;
  }

  @Override
  public Money reduce(Bank bank, String to) {
    int rate = bank.rate(currency, to);
    return new Money(amount / rate, to);
  }
}
