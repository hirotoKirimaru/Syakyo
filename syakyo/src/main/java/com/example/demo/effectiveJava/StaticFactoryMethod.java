package com.example.demo.effectiveJava;

import java.io.BufferedReader;
import java.io.IOException;
import java.lang.reflect.Array;
import java.math.BigInteger;
import java.net.URI;
import java.nio.file.FileStore;
import java.nio.file.Files;
import java.nio.file.Path;
import java.time.Instant;
import java.time.LocalDateTime;
import java.util.*;

/**
 * 第二章項目1
 */
public class StaticFactoryMethod {
  // コンストラクタよりもstaticメソッドを検討する
  // staticファクトリメソッドの共通する命名規約
  public void apply() throws IOException {

    // from:単一のパラメータを受け取り等の型を持つ対応スリンスタンスを返す型変換メソッド(type-conversion method)
    Date d = Date.from(Instant.MIN);

    // of: 服須のパラメータを受け取り、それらを含んだ等の型のインスタンスを返す集約メソッド(aggregation method)
    LocalDateTime date = LocalDateTime.of(2020,1,2,3,4,5);

    // valueOf:fromやofの代わりとなる冗長な名前のメソッド
    BigInteger prime = BigInteger.valueOf(Integer.MAX_VALUE);

    // instance あるいは getInstance: パラメータがあればそのパラメータであらわされているインスタンスを返す。必ずしも同じ値を持つとは限らない。
    StackWalker luke = StackWalker.getInstance(EnumSet.noneOf(StackWalker.Option.class));

    // create　あるいは newInstance: instanceやgetInstanceに似ていますが、呼び出しごとにメソッドは新たなインスタンスを返します。
//    Object newArray = Array.newInstance(classObject, arrayLen);

//    getType: getInstanceに似ているが、ファクトリ目祖度が対象のクラスとは異なるクラスにある場合に使われます。Typeはファクトリメソッドから返されるオブジェクトの型を示しています。
    Path path = Path.of(URI.create(""));
    FileStore fs = Files.getFileStore(path);

    // newType: newInstanceに似ていますが、ファクトリメソッドが対象のクラスとは異なるクラスにある場合に使われます。Typeはファクトリメソッドから返されるオブジェクトの型を示している。
    BufferedReader br = Files.newBufferedReader(path);

//    type:getTypeやnewTypeの代わりとなる簡潔な名前のメソッドです
//    List<Rank> litany = Collections.list(LegacyLitany);

  }

  public static class Rank{

  }




}
