package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var (
	scanner  = bufio.NewScanner(os.Stdin)
	w        = bufio.NewWriter(os.Stdout)
	visited  [1000001]bool
	parent   [1000001]int
	ans, q   []int
	n, count int
)

func main() {
	defer w.Flush()
	scanner.Scan()
	n, _ := strconv.Atoi(scanner.Text())

	bfs(n)
	fmt.Fprintln(w, len(ans)-1)
	for i := len(ans) - 1; i >= 0; i-- {
		fmt.Fprintf(w, "%d ", ans[i])
	}
}

func bfs(v int) {
	q = append(q, v)
	visited[v] = true
	for len(q) > 0 {
		v = q[0]
		q = q[1:]

		if v == 1 {
			ans = append(ans, v)
			for parent[v] != 0 {
				ans = append(ans, parent[v])
				v = parent[v]
			}
			return
		}

		if v%3 == 0 {
			if !visited[v/3] {
				q = append(q, v/3)
				visited[v/3] = true
				parent[v/3] = v
			}
		}
		if v%2 == 0 {
			if !visited[v/2] {
				q = append(q, v/2)
				visited[v/2] = true
				parent[v/2] = v
			}
		}
		if !visited[v-1] {
			q = append(q, v-1)
			visited[v-1] = true
			parent[v-1] = v
		}
	}
}
