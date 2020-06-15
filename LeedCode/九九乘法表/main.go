package main

import (
	"fmt"
)

func main() {
	/* local variable definition */
	var top int = 10
	/*两层循环打印*/
	for i := 1; i < top; i++ {
		for j := 1; j <= i; j++ {
			fmt.Printf("%d * %d = %2d\t", j, i, j*i)
		}
		println()
	}
}

