package com.example.demo.effectiveJava.second_2;

import java.util.EnumSet;
import java.util.Objects;
import java.util.Set;

public abstract class Pizza {
  public enum Topping {HAM, MUSHROOM, ONION, PEPPER, SAUSAGE}
  final Set<Topping> toppings;

  abstract static class Builder<T extends Builder<T>>{
    EnumSet<Topping> toppings = EnumSet.noneOf(Topping.class);
    public T addTopping(Topping topping){
      toppings.add(Objects.requireNonNull(topping));
      return self();
    }

    abstract Pizza build();
    // thisを返すために、サブクラスはこのメソッドをオーバーライドしなければならない。
    // Javaが自分型を持たないことに値する回避策は、疑似自分型イディオムと呼ばれる。
    protected abstract T self();
  }

  Pizza(Builder<?> builder){
    toppings = builder.toppings.clone();
  }
}
