package com.example.demo.tdd;

public class Sum implements Expression {
  /**
   * 被加算数(足し算で足される方の数)
   */
  Expression augend;
  /**
   * 加数
   */
  Expression addend;

  public Sum(Expression augend, Expression addend) {
    this.augend = augend;
    this.addend = addend;
  }

  public Money reduce(Bank bank, String to) {
    int amount = augend.reduce(bank, to).amount + addend.reduce(bank, to).amount;
    return new Money(amount, to);
  }

  @Override
  public Expression plus(Expression addend) {
    return null;
  }
}
