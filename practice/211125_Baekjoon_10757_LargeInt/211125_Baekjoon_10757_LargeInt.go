package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
)

// func main() {
// 	a := new(big.Int)
// 	b := new(big.Int)
// 	sum := new(big.Int)
// 	fmt.Scan(a, b)
// 	fmt.Println(sum.Add(a, b))
// }

func main() {
	var a, b big.Int
	r := bufio.NewReader(os.Stdin)
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	fmt.Fscan(r, &a, &b)
	fmt.Fprint(w, a.Add(&a, &b))
}
