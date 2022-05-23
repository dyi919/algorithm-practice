package main

import (
	"bufio"
	"fmt"
	"os"
)

type pos struct {
	y int
	x int
}

var sum int = 0

func main() {
	var n int
	w := bufio.NewWriter(os.Stdout)
	r := bufio.NewReader(os.Stdin)
	defer w.Flush()
	fmt.Fscan(r, &n)
	board := make([][]bool, n)
	for i := range board {
		board[i] = make([]bool, n)
	}
	solve(board, 0)
	fmt.Fprint(w, sum)
}

func solve(a [][]bool, col int) bool {
	if col == len(a) {
		sum++
		return true
	}

	res := false
	for i := 0; i < len(a); i++ {
		if check(a, pos{i, col}) {
			a[i][col] = true

			res = solve(a, col+1) || res
			a[i][col] = false
		}
	}
	return res
}

func check(a [][]bool, p pos) bool {
	for i := 0; i < len(a[0]); i++ {
		if a[p.y][i] {
			return false
		}
	}

	for i, j := p.y, p.x; i >= 0 && j >= 0; i, j = i-1, j-1 {
		if a[i][j] {
			return false
		}
	}

	for i, j := p.y, p.x; i < len(a) && j >= 0; i, j = i+1, j-1 {
		if a[i][j] {
			return false
		}
	}

	return true
}
