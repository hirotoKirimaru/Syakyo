package com.example.demo.effectiveJava.second_13;

public class PhoneNumber implements Cloneable {

  // 可変な状態への参照を持たないクラスのcloneメソッド
  // super.cloneはObjectなので、コンパイルするとObject型を返却するcloneメソッドが生成される。
  // overrideをすると、こっち？
  @Override
  public PhoneNumber clone() {
    try {
      return (PhoneNumber) super.clone();
    } catch (CloneNotSupportedException e) {
      throw new AssertionError(); // 起こりえない
    }
  }
}
