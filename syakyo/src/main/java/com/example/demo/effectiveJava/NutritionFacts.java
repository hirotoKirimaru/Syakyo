package com.example.demo.effectiveJava;

public class NutritionFacts {
  // ビルダーパターン
  private final int servingSize;// ml (必須）
  private final int servings;// 容器当たり 必須
  private final int fat;// 容器当たり 必須
  private final int calories;// g/一食当たり　オプション
  private final int sodium; // mg/一食当たり　オプション
  private final int carbohydrate;// g/一食当たり　オプション

  public static class Builder {
    // 必須パラメータ
    private final int servingSize;// ml (必須）
    private final int servings;// 容器当たり 必須
    // オプションパラメータ：デフォルト値に初期化
    private int fat = 0;// 容器当たり 必須
    private int calories = 0;// g/一食当たり　オプション
    private int sodium = 0; // mg/一食当たり　オプション
    private int carbohydrate = 0;// g/一食当たり　オプション

    public Builder(int servingSize, int servings) {
      this.servingSize = servingSize;
      this.servings = servings;
    }

    public Builder calories(int val) {
      this.calories = val;
      return this;
    }

    public Builder fat(int val) {
      this.fat = val;
      return this;
    }

    public Builder sodium(int val) {
      this.sodium = val;
      return this;
    }

    public Builder carbohydrate(int val) {
      this.carbohydrate = val;
      return this;
    }

    public NutritionFacts build() {
      return new NutritionFacts(this);
    }
  }

  private NutritionFacts(Builder builder) {
    servingSize = builder.servingSize;
    servings = builder.servings;
    calories = builder.calories;
    fat = builder.fat;
    sodium = builder.sodium;
    carbohydrate = builder.carbohydrate;
  }


  public void use() {
    // 流れるようなAPI: fluentAPIになる
    NutritionFacts cocaCola = new Builder(240, 8)
        .calories(100)
        .sodium(35)
        .carbohydrate(27)
        .build();

  }
}
