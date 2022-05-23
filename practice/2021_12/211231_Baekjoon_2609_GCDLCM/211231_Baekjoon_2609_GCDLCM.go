package main

import (
	"bufio"
	"fmt"
	"os"
)

var scanner = bufio.NewScanner(os.Stdin)

func main() {
	var g int
	w := bufio.NewWriter(os.Stdout)
	scanner.Split(bufio.ScanWords)
	defer w.Flush()
	a, b := nextInt(), nextInt()
	if a < b {
		a, b = b, a
	}
	g = gcd(a, b)
	fmt.Fprintln(w, g)
	fmt.Fprintln(w, a*b/g)
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
