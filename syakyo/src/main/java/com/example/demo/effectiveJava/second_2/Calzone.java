package com.example.demo.effectiveJava.second_2;

import java.util.Objects;

/**
 * カルツォーネ
 * ソースが中か外化を指定する
 */
public class Calzone extends Pizza {
  private final boolean sauceInside;

  public static class Builder extends Pizza.Builder<Builder>{
    private boolean sauceInside = false;// デフォルト

    public Builder sauceInside(){
      sauceInside = true;
      return this;
    }

    @Override
    public Calzone build(){
      // スーパークラスの宣言された戻り値型のサブタイスを返すと宣言するのは、共変戻り値片付け(covariant return typeing)と呼ばれる。
      // クライアントはキャストなしでビルダーを使える。
      return new Calzone(this);
    }
    @Override
    protected Builder self(){
      return this;
    }
  }
  private Calzone(Builder builder){
    super(builder);
    sauceInside = builder.sauceInside;
  }
}
