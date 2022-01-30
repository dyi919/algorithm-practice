package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	scanner           = bufio.NewScanner(os.Stdin)
	w                 = bufio.NewWriter(os.Stdout)
	g                 [][]int
	visited, compared []bool
	stack             []int
	n, m              int
)

func main() {
	defer w.Flush()
	scanner.Split(bufio.ScanWords)
	n, m = nextInt(), nextInt()
	visited = make([]bool, n+1)
	compared = make([]bool, n+1)
	g = make([][]int, n+1)

	for i := 0; i < m; i++ {
		k := nextInt()
		a := nextInt()
		for j := 1; j < k; j++ {
			b := nextInt()
			compared[a], compared[b] = true, true
			g[a] = append(g[a], b)
			a = b
		}
	}
	for key := 1; key < n+1; key++ {
		if len(g[key]) > 0 {
			if !visited[key] {
				topologicalSort(key)
			}
		}
	}
	if isCycle() {
		fmt.Fprintln(w, 0)
		return
	}
	for i := 1; i < n+1; i++ {
		if !compared[i] {
			fmt.Fprintln(w, i)
		}
	}
	for i := len(stack) - 1; i >= 0; i-- {
		fmt.Fprintln(w, stack[i])
	}
}

func isCycle() bool {
	pos := make([]int, n+1)
	idx := 1
	for i := len(stack) - 1; i >= 0; i-- {
		pos[stack[i]] = idx
		idx++
	}
	for i := 1; i < n+1; i++ {
		for _, j := range g[i] {
			first, second := 0, 0
			if pos[i] != 0 {
				first = pos[i]
			}
			if pos[j] != 0 {
				second = pos[j]
			}
			if first > second {
				return true
			}
		}
	}
	return false
}

func topologicalSort(v int) {
	visited[v] = true

	for i := range g[v] {
		if !visited[g[v][i]] {
			topologicalSort(g[v][i])
		}
	}
	stack = append(stack, v)
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
