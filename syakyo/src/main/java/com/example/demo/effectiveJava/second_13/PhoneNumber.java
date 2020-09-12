package com.example.demo.effectiveJava.second_13;

public class PhoneNumber {

  // 可変な状態への参照を持たないクラスのcloneメソッド
  @Override
  public PhoneNumber clone() {
    try {
      return (PhoneNumber) super.clone();
    } catch (CloneNotSupportedException e) {
      throw new AssertionError(); // 起こりえない
    }
  }
}
