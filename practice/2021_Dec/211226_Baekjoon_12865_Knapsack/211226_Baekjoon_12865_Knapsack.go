package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var scanner = bufio.NewScanner(os.Stdin)

func main() {
	var w, v int
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	scanner.Split(bufio.ScanWords)
	n, k := nextInt(), nextInt()

	dp := make([]int, k+1)
	for i := 1; i <= n; i++ {
		w, v = nextInt(), nextInt()
		for j := k; j >= w; j-- {
			if dp[j-w]+v > dp[j] {
				dp[j] = dp[j-w] + v
			}
		}
	}
	fmt.Fprint(writer, dp[k])
}

func nextInt() int {
	scanner.Scan()
	r, _ := strconv.Atoi(scanner.Text())
	return r
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
