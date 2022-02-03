package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	scanner = bufio.NewScanner(os.Stdin)
	w       = bufio.NewWriter(os.Stdout)
	board   [][]byte
	di, dj  [4]int
	visited [26]bool
	r, c    int
	maxCnt  = 0
)

func main() {
	defer w.Flush()
	scanner.Split(bufio.ScanWords)

	r, c = nextInt(), nextInt()
	board = make([][]byte, r)
	di = [4]int{0, 0, -1, 1}
	dj = [4]int{-1, 1, 0, 0}
	cnt := 0

	for i := 0; i < r; i++ {
		scanner.Scan()
		board[i] = []byte(scanner.Text())
	}

	visited[board[0][0]-'A'] = true
	cnt++
	dfs(0, 0, cnt)

	fmt.Fprintln(w, maxCnt)
}

func dfs(i, j, cnt int) {
	maxCnt = max(maxCnt, cnt)

	for k := 0; k < 4; k++ {
		ki, kj := i+di[k], j+dj[k]
		if canVisit(ki, kj) {
			visited[board[ki][kj]-'A'] = true
			dfs(ki, kj, cnt+1)
			visited[board[ki][kj]-'A'] = false
		}
	}
}

func canVisit(i, j int) bool {
	if i < 0 || j < 0 || i >= r || j >= c {
		return false
	} else if !visited[board[i][j]-'A'] {
		return true
	}
	return false
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
