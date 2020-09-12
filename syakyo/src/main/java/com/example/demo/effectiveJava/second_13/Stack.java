package com.example.demo.effectiveJava.second_13;

public class Stack implements Cloneable {
  private Object[] elements;
  private int size = 0;
  private static final int DEFAULT_INITIAL_CAPACITY = 16;

  @Override
  public Stack clone() {
    try {
      Stack result = (Stack) super.clone();
      result.elements = elements.clone(); // 配列はキャストせずにcloneできる。
      return result;
    } catch (CloneNotSupportedException e) {
      throw new AssertionError(); // 起こりえない
    }
  }
}
