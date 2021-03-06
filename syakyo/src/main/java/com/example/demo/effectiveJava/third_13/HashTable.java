package com.example.demo.effectiveJava.third_13;

public class HashTable implements Cloneable {
  private Entry[] buckets;

  private static class Entry {
    final Object key;
    Object value;
    Entry next;

    public Entry(Object key, Object value, Entry next) {
      this.key = key;
      this.value = value;
      this.next = next;
    }

//    Entry deepCopy() {
//      return new Entry(key, value, next == null ? null : next.deepCopy());
//    }

    // このEntryを先頭とするリンクリストをループしながらコピーする
    Entry deepCopy() {
      Entry result = new Entry(key, value, next);
      for (Entry p = result; p.next != null; p = p.next) p.next = new Entry(p.next.key, p.next.value, p.next.next);
      return result;
    }
  }

  //  // 不完全 - 内部状態が共有されている
//  @Override
//  public HashTable clone() {
//    try {
//      HashTable result = (HashTable) super.clone();
//      result.buckets = buckets.clone();
//      return result;
//    } catch (CloneNotSupportedException e) {
//      throw new AssertionError(); // 起こりえない
//    }
//  }
// 不完全 - 内部状態が共有されている
  @Override
  public HashTable clone() {
    try {
      HashTable result = (HashTable) super.clone();
      result.buckets = new Entry[buckets.length];
      // リンクリストを複製した時は、スタックフレームを消費するから、リストが長いとスタックオーバーフローを起こしうる。
      for (int i = 0; i < buckets.length; i++) {
        if (buckets[i] != null) result.buckets[i] = buckets[i].deepCopy();
      }
      return result;
    } catch (CloneNotSupportedException e) {
      throw new AssertionError(); // 起こりえない
    }
  }
}
