package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var n, count int
	w := bufio.NewWriter(os.Stdout)
	r := bufio.NewReader(os.Stdin)
	defer w.Flush()
	fmt.Fscan(r, &n)
	dp := make([]map[int]bool, 0)
	dp = append(dp, make(map[int]bool))
	dp[0][n] = true

	for !dp[count][1] {
		dp = append(dp, make(map[int]bool))
		count++
		for v := range dp[count-1] {
			if v%3 == 0 {
				dp[count][v/3] = true
			}
			if v%2 == 0 {
				dp[count][v/2] = true
			}
			dp[count][v-1] = true
		}
	}

	fmt.Fprint(w, count)
}
