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
	var s1, s2 string
	defer w.Flush()
	scanf("%s\n", &s1)
	scanf("%s\n", &s2)
	var dp [1001][1001]int
	for i := 1; i <= len(s1); i++ {
		for j := 1; j <= len(s2); j++ {
			if s1[i-1] == s2[j-1] {
				dp[i][j] = dp[i-1][j-1] + 1
			} else {
				dp[i][j] = max(dp[i][j-1], dp[i-1][j])
			}
		}
	}
	printf("%d", dp[len(s1)][len(s2)])
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
