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
	t := nextInt()
	var dp [11]int
	dp[0] = 0
	dp[1] = 1
	dp[2] = 2
	dp[3] = 4
	for i := 4; i < 11; i++ {
		dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
	}
	for i := 0; i < t; i++ {
		n := nextInt()
		fmt.Fprintln(w, dp[n])
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
