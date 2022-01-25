package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	scanner = bufio.NewScanner(os.Stdin)
	w       = bufio.NewWriter(os.Stdout)
	tb, dp  [][]int

	x1, x2, y1, y2 int
)

func main() {
	defer w.Flush()
	scanner.Split(bufio.ScanWords)
	n, m := nextInt(), nextInt()
	tb = make([][]int, n)
	dp = make([][]int, n)
	for i := 0; i < n; i++ {
		tb[i] = make([]int, n)
		dp[i] = make([]int, n)
		for j := 0; j < n; j++ {
			tb[i][j] = nextInt()
			if i == 0 {
				if j == 0 {
					dp[i][j] = tb[i][j]
				} else {
					dp[i][j] = dp[i][j-1] + tb[i][j]
				}
			} else {
				if j == 0 {
					dp[i][j] = dp[i-1][j] + tb[i][j]
				} else {
					dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + tb[i][j]
				}
			}
		}
	}

	for k := 0; k < m; k++ {
		x1, y1, x2, y2 := nextInt()-1, nextInt()-1, nextInt()-1, nextInt()-1
		if x1 == 0 && y1 == 0 {
			fmt.Fprintln(w, dp[x2][y2])
		} else if x1 == 0 {
			fmt.Fprintln(w, dp[x2][y2]-dp[x2][y1-1])
		} else if y1 == 0 {
			fmt.Fprintln(w, dp[x2][y2]-dp[x1-1][y2])
		} else {
			fmt.Fprintln(w, dp[x2][y2]-dp[x2][y1-1]-dp[x1-1][y2]+dp[x1-1][y1-1])
		}
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
