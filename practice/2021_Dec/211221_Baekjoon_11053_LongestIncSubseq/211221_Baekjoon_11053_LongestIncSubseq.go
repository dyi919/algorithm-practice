package main

import (
	"bufio"
	"fmt"
	"os"
)

var r *bufio.Reader = bufio.NewReader(os.Stdin)
var w *bufio.Writer = bufio.NewWriter(os.Stdout)

func printf(f string, a ...interface{}) { fmt.Fprintf(w, f, a...) }
func scanf(f string, a ...interface{})  { fmt.Fscanf(r, f, a...) }

func main() {
	var n, max int
	defer w.Flush()
	scanf("%d\n", &n)

	s, dp := make([]int, n), make([]int, n)

	for i := 0; i < n; i++ {
		scanf("%d ", &s[i])

		dp[i] = 1

		for j := 0; j < i; j++ {
			if s[i] > s[j] && dp[i] < dp[j]+1 {
				dp[i] = dp[j] + 1
			}
		}
		if dp[i] > max {
			max = dp[i]
		}
	}

	fmt.Fprint(w, max)
}
