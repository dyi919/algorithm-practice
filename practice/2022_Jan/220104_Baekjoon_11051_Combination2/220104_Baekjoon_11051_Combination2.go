package main

import (
	"bufio"
	"fmt"
	"os"
)

var scanner = bufio.NewScanner(os.Stdin)

func main() {
	var c [1001][1001]int
	mod := 10007
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	scanner.Split(bufio.ScanWords)
	a, b := nextInt(), nextInt()
	
	c[0][0] = 1
	
	for i := 1; i <= a; i++ {
		c[i][0] = 1
		for j := 1; j <= b; j++{
			c[i][j] = (c[i-1][j-1] + c[i-1][j]) % mod
		}
	}
	fmt.Fprint(w, c[a][b])
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
