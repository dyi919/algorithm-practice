package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

type point struct {
	i int
	j int
}

var scanner = bufio.NewScanner(os.Stdin)

var space [][]int
var count = 0
var size = 2
var pos = point{-1, -1}
var ans = 0

func bfs() bool {
	distance := 0
	visited := make([][]bool, len(space))
	for i := range visited {
		visited[i] = make([]bool, len(space))
		for j := range visited[i] {
			visited[i][j] = false
		}
	}
	queue := make([]point, 0)
	candidates := make([]point, 0)

	queue = append(queue, pos)
	visited[pos.i][pos.j] = true

	for len(queue) > 0 {
		queueSize := len(queue)
		for queueSize > 0 {
			v := queue[0]
			queue = queue[1:]

			if space[v.i][v.j] > 0 && space[v.i][v.j] < size {
				candidates = append(candidates, point{v.i, v.j})
			}

			if v.i > 0 {
				if visited[v.i-1][v.j] == false && space[v.i-1][v.j] <= size {
					queue = append(queue, point{v.i - 1, v.j})
					visited[v.i-1][v.j] = true
				}
			}
			if v.j > 0 {
				if visited[v.i][v.j-1] == false && space[v.i][v.j-1] <= size {
					queue = append(queue, point{v.i, v.j - 1})
					visited[v.i][v.j-1] = true
				}
			}
			if v.i < len(space)-1 {
				if visited[v.i+1][v.j] == false && space[v.i+1][v.j] <= size {
					queue = append(queue, point{v.i + 1, v.j})
					visited[v.i+1][v.j] = true
				}
			}
			if v.j < len(space)-1 {
				if visited[v.i][v.j+1] == false && space[v.i][v.j+1] <= size {
					queue = append(queue, point{v.i, v.j + 1})
					visited[v.i][v.j+1] = true
				}
			}
			queueSize -= 1
		}

		if len(candidates) > 0 {
			choose := candidates[0]
			for i := 1; i < len(candidates); i++ {
				if candidates[i].i < choose.i || (candidates[i].i == choose.i && candidates[i].j < choose.j) {
					choose = candidates[i]
				}
			}
			eat(choose, distance)
			return true
		}

		distance += 1

	}
	return false
}

func eat(target point, distance int) {
	space[pos.i][pos.j] = 0
	space[target.i][target.j] = 9
	ans += distance
	if size < 7 {
		count += 1
		if count == size {
			size += 1
			count = 0
		}
	}
	pos.i, pos.j = target.i, target.j
}

func main() {
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	scanner.Split(bufio.ScanWords)
	scanner.Scan()
	n, _ := strconv.Atoi(scanner.Text())
	space = make([][]int, n)
	for i := 0; i < n; i++ {
		space[i] = make([]int, n)
		for j := 0; j < n; j++ {
			scanner.Scan()
			space[i][j], _ = strconv.Atoi(scanner.Text())
			if space[i][j] == 9 {
				pos = point{i, j}
			}
		}
	}
	for {
		if !bfs() {
			fmt.Fprintln(w, ans)
			break
		}
	}
}
