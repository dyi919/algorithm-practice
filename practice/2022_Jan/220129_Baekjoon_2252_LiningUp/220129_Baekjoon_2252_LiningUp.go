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
)

func main() {
	defer w.Flush()
	scanner.Split(bufio.ScanWords)
	n, m := nextInt(), nextInt()
	visited = make([]bool, n+1)
	compared = make([]bool, n+1)
	g = make([][]int, n+1)

	for i := 0; i < m; i++ {
		a, b := nextInt(), nextInt()
		compared[a], compared[b] = true, true
		g[a] = append(g[a], b)
	}
	for key := 1; key < n+1; key++ {
		if len(g[key]) > 0 {
			if !visited[key] {
				topologicalSort(key)
			}
		} else if !compared[key] {
			fmt.Fprintf(w, "%d ", key)
		}
	}
	for i := len(stack) - 1; i >= 0; i-- {
		fmt.Fprintf(w, "%d ", stack[i])
	}
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
