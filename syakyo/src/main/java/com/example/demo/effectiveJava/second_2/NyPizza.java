package com.example.demo.effectiveJava.second_2;

import java.util.Objects;

/**
 * ニューヨークスタイルのピザ
 * 大きさのパラメータの指定を必要とする。
 */
public class NyPizza extends Pizza {
  public enum Size {SMALL, MEDIUM, LARGE}
  private final Size size;

  public static class Builder extends Pizza.Builder<Builder>{
    private final Size size;
    public Builder(Size size){
      this.size = Objects.requireNonNull(size);
    }
    @Override
    public NyPizza build(){
      return new NyPizza(this);
    }
    @Override
    protected Builder self(){
      return this;
    }
  }
  public NyPizza(Builder builder){
    super(builder);
    size = builder.size;
  }
}