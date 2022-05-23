package main

import (
	"bufio"
	"fmt"
	"os"
)

var scanner = bufio.NewScanner(os.Stdin)

func main() {
	totalCost := 0
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	scanner.Split(bufio.ScanWords)
	n := nextInt() - 1
	dist := make([]int, n)
	for i := 0; i < n; i++ {
		dist[i] = nextInt()
	}

	currentPrice := nextInt()
	totalCost += currentPrice * dist[0]
	for i := 1; i < n; i++ {
		nextPrice := nextInt()
		if nextPrice < currentPrice {
			currentPrice = nextPrice
		}
		totalCost += currentPrice * dist[i]
	}

	fmt.Fprint(w, totalCost)
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
