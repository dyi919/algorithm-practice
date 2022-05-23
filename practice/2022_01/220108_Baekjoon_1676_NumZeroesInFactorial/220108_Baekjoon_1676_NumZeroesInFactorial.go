package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
)

var scanner = bufio.NewScanner(os.Stdin)

func main() {
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	scanner.Split(bufio.ScanWords)
	n := nextInt()
	if n < 5 {
		fmt.Fprint(w, "0")
	} else {
		factorial := new(big.Int)
		factorial.MulRange(1, int64(n))
		factorialStr := factorial.String()
		cnt := 0
		for factorialStr[len(factorialStr)-1] == 48 {
			factorialStr = factorialStr[:len(factorialStr)-1]
			cnt++
		}
		fmt.Fprint(w, cnt)
	}
}

func nextInt() int {
	scanner.Scan()
	r := 0
	for _, c := range scanner.Bytes() {
		r *= 10
		r += int(c - '0')
	}
	return r
}
