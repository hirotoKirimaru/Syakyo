package com.example.demo.tdd;

public class Sum implements Expression {
  /**
   * 被加算数(足し算で足される方の数)
   */
  Money augend;
  /**
   * 加数
   */
  Money addend;

  public Sum(Money augend, Money addend) {
    this.augend = augend;
    this.addend = addend;
  }

  public Money reduce(Bank bank, String to) {
    int amount = augend.amount + addend.amount;
    return new Money(amount, to);
  }
}
