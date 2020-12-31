package main

import "fmt"

// 同じ型なら省略可能
func add(x, y int) int {
	return x + y
}

func main() {
	fmt.Println(add(42, 13))
}
