package main

import (
	"bufio"
	"fmt"
	"os"
)

var scanner = bufio.NewScanner(os.Stdin)

func main() {
	var dp [10000][3]int
	var v int
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	scanner.Split(bufio.ScanWords)
	n := nextInt()
	if n == 1 {
		v = nextInt()
		fmt.Fprint(w, v)
	} else if n == 2 {
		v = nextInt() + nextInt()
		fmt.Fprint(w, v)
	} else {
		dp[0][1] = nextInt()
		for i := 1; i < n; i++ {
			v = nextInt()
			dp[i][0] = max(dp[i-1][0], max(dp[i-1][1], dp[i-1][2]))
			dp[i][1] = dp[i-1][0] + v
			dp[i][2] = dp[i-1][1] + v
		}
		fmt.Fprint(w, max(dp[n-1][0], max(dp[n-1][1], dp[n-1][2])))
	}
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
