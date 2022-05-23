package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var n, priceR, priceG, priceB int
	w := bufio.NewWriter(os.Stdout)
	r := bufio.NewReader(os.Stdin)
	defer w.Flush()
	fmt.Fscan(r, &n)
	dpR := make([]int, n)
	dpG := make([]int, n)
	dpB := make([]int, n)
	fmt.Fscan(r, &dpR[0], &dpG[0], &dpB[0])
	for i := 1; i < n; i++ {
		fmt.Fscan(r, &priceR, &priceG, &priceB)
		dpR[i] = min(dpG[i-1], dpB[i-1]) + priceR
		dpG[i] = min(dpR[i-1], dpB[i-1]) + priceG
		dpB[i] = min(dpR[i-1], dpG[i-1]) + priceB
	}
	fmt.Fprint(w, min(min(dpR[n-1], dpG[n-1]), dpB[n-1]))
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
