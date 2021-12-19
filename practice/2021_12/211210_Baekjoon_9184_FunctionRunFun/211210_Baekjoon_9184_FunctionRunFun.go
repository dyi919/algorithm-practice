package main

import (
	"bufio"
	"fmt"
	"os"
)

var s [][][]int

func main() {
	var a, b, c int
	r := bufio.NewReader(os.Stdin)
	wr := bufio.NewWriter(os.Stdout)
	defer wr.Flush()
	s = make([][][]int, 21)
	for i := range s {
		s[i] = make([][]int, 21)
		for j := range s[i] {
			s[i][j] = make([]int, 21)
		}
	}
	for {
		fmt.Fscan(r, &a, &b, &c)
		if a == -1 && b == -1 && c == -1 {
			break
		}
		fmt.Fprintf(wr, "w(%d, %d, %d) = %d\n", a, b, c, w(a, b, c))
	}
}

func w(a, b, c int) int {
	if a <= 0 || b <= 0 || c <= 0 {
		return 1
	}
	if a > 20 || b > 20 || c > 20 {
		return w(20, 20, 20)
	}
	if s[a][b][c] != 0 {
		return s[a][b][c]
	}
	var v int
	if a < b && b < c {
		v = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
		if s[a][b][c] == 0 {
			s[a][b][c] = v
		}
		return v
	}
	v = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
	if s[a][b][c] == 0 {
		s[a][b][c] = v
	}
	return v
}
