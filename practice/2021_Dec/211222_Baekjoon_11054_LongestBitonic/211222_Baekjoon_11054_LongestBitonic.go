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

	s, dpUp, dpDown := make([]int, n), make([]int, n), make([]int, n)

	for i := 0; i < n; i++ {
		scanf("%d ", &s[i])

		dpUp[i] = 1
		dpDown[i] = 1
	}

	for i := 0; i < n; i++ {
		for j := 0; j < i; j++ {
			if s[i] > s[j] && dpUp[i] < dpUp[j]+1 {
				dpUp[i] = dpUp[j] + 1
			}
		}
	}
	for i := n - 1; i >= 0; i-- {
		for j := n - 1; j > i; j-- {
			if s[i] > s[j] && dpDown[i] < dpDown[j]+1 {
				dpDown[i] = dpDown[j] + 1
			}
		}
		v := dpUp[i] + dpDown[i] - 1
		if v > max {
			max = v
		}
	}
	fmt.Fprint(w, max)
}
