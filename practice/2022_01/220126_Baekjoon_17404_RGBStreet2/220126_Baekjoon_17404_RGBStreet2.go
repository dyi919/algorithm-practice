package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var n int
	w := bufio.NewWriter(os.Stdout)
	r := bufio.NewReader(os.Stdin)
	defer w.Flush()
	fmt.Fscan(r, &n)
	var dp [1001][3]int
	var price [1001][3]int
	for i := 1; i <= n; i++ {
		fmt.Fscan(r, &price[i][0], &price[i][1], &price[i][2])
	}
	minVal := 1000001

	for k := 0; k < 3; k++ {
		for i := 0; i < 3; i++ {
			if i == k {
				dp[1][i] = price[1][i]
			} else {
				dp[1][i] = 1000001
			}
		}
		for i := 2; i <= n; i++ {
			dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + price[i][0]
			dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + price[i][1]
			dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + price[i][2]
		}
		for i := 0; i < 3; i++ {
			if i == k {
				continue
			}
			minVal = min(minVal, dp[n][i])
		}
	}

	fmt.Fprintln(w, minVal)
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
