package com.example.demo.effectiveJava.second_13;

/**
 * 13の結論。Cloneableやめろ。
 */
public class Clone implements Cloneable {
  // Cloneable をサポートしない拡張可能なクラス用のcloneメソッド
  @Override
  protected final Object clone() throws CloneNotSupportedException{
    throw new CloneNotSupportedException();
  }

  public Clone(){
  }

  // コピーコンストラクタ
  public Clone(Clone clone){
    // いいかんじ
  }

  // コピーファクトリ
  public static Clone newInstance(Clone clone){
    // いいかんじ
    return new Clone();
  }
}
