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
	
	var c [31][31]int
	c[0][0] = 1
	
	for i := 1; i <= 30; i++ {
		c[i][0] = 1
		for j := 1; j <= 30; j++{
			c[i][j] = (c[i-1][j-1] + c[i-1][j])
		}
	}
	for i := 0; i < n; i++ {
		a, b := nextInt(), nextInt()
		fmt.Fprintln(w, c[b][a])
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
