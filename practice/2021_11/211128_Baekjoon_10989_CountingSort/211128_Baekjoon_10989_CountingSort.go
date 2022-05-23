package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var n, v int
	r := bufio.NewReader(os.Stdin)
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	fmt.Fscan(r, &n)
	s := make([]int, 10001)
	for i := 0; i < n; i++ {
		fmt.Fscan(r, &v)
		s[v]++
	}
	for i := 1; i < 10001; i++ {
		for s[i] > 0 {
			fmt.Fprintln(w, i)
			s[i]--
		}
	}
}
