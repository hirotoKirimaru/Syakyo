package com.example.demo.effectiveJava.second_2;

public class PizzaUse {

  void use(){
    NyPizza pizza = new NyPizza
        .Builder(NyPizza.Size.SMALL)
        .addTopping(Pizza.Topping.SAUSAGE)
        .addTopping(Pizza.Topping.ONION)
        .build();

    Calzone calzone = new Calzone
        .Builder()
        .addTopping(Pizza.Topping.HAM)
        .sauceInside()
        .build();
  }
}
