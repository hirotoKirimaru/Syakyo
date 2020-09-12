package com.example.demo.effectiveJava.second_13;

public class HashTable implements Cloneable {
  private Entry[] buckets;

  private static class Entry{
    final Object key;
    Object value;
    Entry next;

    public Entry(Object key, Object value, Entry next) {
      this.key = key;
      this.value = value;
      this.next = next;
    }
  }

  // 不完全 - 内部状態が共有されている
  @Override
  public HashTable clone() {
    try {
      HashTable result = (HashTable) super.clone();
      result.buckets = buckets.clone();
      return result;
    } catch (CloneNotSupportedException e) {
      throw new AssertionError(); // 起こりえない
    }
  }
}
