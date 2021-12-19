package main

import (
	"bufio"
	"fmt"
	"os"
)

var w = bufio.NewWriter(os.Stdout)

func main() {
	var n, m int
	r := bufio.NewReader(os.Stdin)
	defer w.Flush()
	fmt.Fscan(r, &n, &m)
	a := make([]int, m)
	permutation(a, 0, 0, n, m)
}

func permutation(a []int, pos, prev, n, m int) {
	if pos == m {
		for i := 0; i < m; i++ {
			fmt.Fprintf(w, "%d ", a[i])
		}
		fmt.Fprintln(w)
	} else {
		for i := prev; i < n; i++ {
			a[pos] = i + 1
			permutation(a, pos+1, i, n, m)
		}
	}
}
