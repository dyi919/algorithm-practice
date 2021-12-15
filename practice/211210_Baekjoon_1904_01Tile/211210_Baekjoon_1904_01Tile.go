package main

import (
	"bufio"
	"fmt"
	"os"
)

var dp []int

func main() {
	var n int
	w := bufio.NewWriter(os.Stdout)
	r := bufio.NewReader(os.Stdin)
	defer w.Flush()
	fmt.Fscan(r, &n)
	dp = make([]int, 1000001)
	fmt.Fprint(w, tile(n))
}

func tile(n int) int {
	if n == 1 {
		return 1
	}
	if n == 2 {
		return 2
	}
	if dp[n] != 0 {
		return dp[n] % 15746
	}
	v := (tile(n-1) + tile(n-2)) % 15746
	dp[n] = v
	return v
}
