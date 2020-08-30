package com.example.demo.effectiveJava;

import lombok.NoArgsConstructor;
import lombok.Setter;

import java.io.BufferedReader;
import java.io.IOException;
import java.math.BigInteger;
import java.net.URI;
import java.nio.file.FileStore;
import java.nio.file.Files;
import java.nio.file.Path;
import java.time.Instant;
import java.time.LocalDateTime;
import java.util.Date;
import java.util.EnumSet;

/**
 * 第二章項目2 多くのコンストラクタパラメータに直面した時にはビルダーを検討する。
 */
public class Builder {

  // テレスコーピング・コンストラクタ・パターン(うまく対応できない)
  public class NutritionFacts_1 {
    private final int serbingSize;// ml (必須）
    private final int servings;// 容器当たり 必須
    private final int fat;// 容器当たり 必須
    private final int calories;// g/一食当たり　オプション
    private final int sodium; // mg/一食当たり　オプション
    private final int carbohydrate;// g/一食当たり　オプション

    public NutritionFacts_1(int serbingSize, int servings) {
      this(serbingSize, servings, 0);
    }

    public NutritionFacts_1(int serbingSize, int servings, int calories) {
      this(serbingSize, servings, calories, 0);
    }

    public NutritionFacts_1(int serbingSize, int servings, int calories, int fat) {
      this(serbingSize, servings, calories, fat, 0);
    }

    public NutritionFacts_1(int serbingSize, int servings, int calories, int fat, int sodium) {
      this(serbingSize, servings, calories, fat, sodium, 0);
    }

    public NutritionFacts_1(int serbingSize, int servings, int calories, int fat, int sodium, int carbohydrate) {
      this.serbingSize = serbingSize;
      this.servings = servings;
      this.calories = calories;
      this.fat = fat;
      this.sodium = sodium;
      this.carbohydrate = carbohydrate;
    }
  }

  // JavaBeansパターン：不整合を許し、可変性を必要とする
  @NoArgsConstructor
  @Setter
  public class NutritionFacts_2 {
    // （あれば）デフォルト値でパラメータを初期化する
    private int serbingSize = -1;// ml (必須）
    private int servings = -1;// 容器当たり 必須
    private int fat = 0;// 容器当たり 必須
    private int calories = 0;// g/一食当たり　オプション
    private int sodium = 0; // mg/一食当たり　オプション
    private int carbohydrate = 0;// g/一食当たり　オプション

  }

  public void _2(){
    NutritionFacts_2 cocaCola = new NutritionFacts_2();
    cocaCola.setSerbingSize(240);
    cocaCola.setServings(8);
    cocaCola.setCalories(100);
    cocaCola.setSodium(35);
    cocaCola.setCarbohydrate(27);
  }

}
