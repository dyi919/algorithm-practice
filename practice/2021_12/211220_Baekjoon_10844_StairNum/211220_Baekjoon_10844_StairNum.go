package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	div := 1000000000
	var dp [101][10]int
	var ans, n int
	w := bufio.NewWriter(os.Stdout)
	r := bufio.NewReader(os.Stdin)
	defer w.Flush()
	fmt.Fscan(r, &n)
	dp[1] = [10]int{0, 1, 1, 1, 1, 1, 1, 1, 1, 1}
	for i := 2; i <= n; i++ {
		dp[i][0] = dp[i-1][1]
		for j := 1; j <= 8; j++ {
			dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % div
		}
		dp[i][9] = dp[i-1][8]
	}
	for i := range dp[n] {
		ans = (ans + dp[n][i]) % div
	}
	fmt.Fprint(w, ans)
}
