package com.example.demo.tdd;

public interface Expression {
  Money reduce(Bank bank, String to);

  default Expression plus(Expression addend) {
    return new Sum(this, addend);
  }

  Expression times(int multipiler);
}
