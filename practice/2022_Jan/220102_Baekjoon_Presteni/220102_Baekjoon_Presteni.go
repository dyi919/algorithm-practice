package main

import (
	"bufio"
	"fmt"
	"os"
)

var scanner = bufio.NewScanner(os.Stdin)

func main() {
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	scanner.Split(bufio.ScanWords)
	n := nextInt()
	firstRing := nextInt()
	for i := 1; i < n; i++ {
		numerator := firstRing
		denominator := nextInt()
		g := gcd(numerator, denominator)
		fmt.Fprintf(w, "%d/%d\n", numerator/g, denominator/g)
	}
}

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
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
