package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

var r *bufio.Reader = bufio.NewReader(os.Stdin)
var w *bufio.Writer = bufio.NewWriter(os.Stdout)

func printf(f string, a ...interface{}) { fmt.Fprintf(w, f, a...) }
func scanf(f string, a ...interface{})  { fmt.Fscanf(r, f, a...) }

func main() {
	var n, max int
	defer w.Flush()
	scanf("%d\n", &n)

	s := make([][]int, n)
	dp := make([]int, n)

	for i := 0; i < n; i++ {
		s[i] = make([]int, 2)
		scanf("%d %d\n", &s[i][0], &s[i][1])
		dp[i] = 1
	}

	sort.Slice(s, func(i, j int) bool {
		return s[i][0] < s[j][0]
	})

	for i := 0; i < n; i++ {

		for j := 0; j < i; j++ {
			if (s[j][0] > s[i][0] && s[j][1] > s[i][1]) || (s[j][0] < s[i][0] && s[j][1] < s[i][1]) && dp[i] < dp[j]+1 {
				dp[i] = dp[j] + 1
			}
		}
		if dp[i] > max {
			max = dp[i]
		}
	}

	fmt.Fprint(w, n-max)
}
