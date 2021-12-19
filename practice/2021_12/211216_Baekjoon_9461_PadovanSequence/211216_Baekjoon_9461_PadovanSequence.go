package main

import (
	"bufio"
	"fmt"
	"os"
)

var p []int

func main() {
	var t, n int
	w := bufio.NewWriter(os.Stdout)
	r := bufio.NewReader(os.Stdin)
	defer w.Flush()
	fmt.Fscan(r, &t)
	p = make([]int, 101)
	for i := 0; i < t; i++ {
		fmt.Fscan(r, &n)
		fmt.Fprintln(w, padovan(n))
	}
}

func padovan(n int) int {
	if n < 1 {
		return 0
	}
	if n < 4 {
		return 1
	}
	if n < 6 {
		return 2
	}
	if p[n] != 0 {
		return p[n]
	}
	v := padovan(n-1) + padovan(n-5)
	p[n] = v
	return v
}
