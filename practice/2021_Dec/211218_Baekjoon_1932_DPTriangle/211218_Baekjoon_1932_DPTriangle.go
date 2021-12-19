package main

import (
	"bufio"
	"fmt"
	"os"
)

var scanner = bufio.NewScanner(os.Stdin)

func main() {
	var dp [501][501]int
	sum := 0
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	scanner.Split(bufio.ScanWords)
	n := nextInt()
	dp[0][0] = 0
	dp[0][1] = 0
	for i := 1; i <= n; i++ {
		for j := 1; j <= i; j++ {
			dp[i][j] = nextInt()
			if j == 1 {
				dp[i][j] = dp[i-1][j] + dp[i][j]
			} else if j == i {
				dp[i][j] = dp[i-1][j-1] + dp[i][j]
			} else {
				dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + dp[i][j]
			}

			if dp[i][j] > sum {
				sum = dp[i][j]
			}
		}
	}
	fmt.Fprint(w, sum)
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
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
