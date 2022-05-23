package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

type pos struct {
	i int
	j int
	k int
}

var scanner = bufio.NewScanner(os.Stdin)
var box [][][]int
var days [][][]int

func bfs(startPos pos) {
	queue := make([]pos, 0)

	queue = append(queue, startPos)

	day := 1
	for len(queue) > 0 {
		queueSize := len(queue)
		for queueSize > 0 {
			t := queue[0]
			queue = queue[1:]

			if t.i > 0 {
				if check(pos{t.i - 1, t.j, t.k}, day) {
					queue = append(queue, pos{t.i - 1, t.j, t.k})
					days[t.i-1][t.j][t.k] = day
				}
			}
			if t.j > 0 {
				if check(pos{t.i, t.j - 1, t.k}, day) {
					queue = append(queue, pos{t.i, t.j - 1, t.k})
					days[t.i][t.j-1][t.k] = day
				}
			}
			if t.k > 0 {
				if check(pos{t.i, t.j, t.k - 1}, day) {
					queue = append(queue, pos{t.i, t.j, t.k - 1})
					days[t.i][t.j][t.k-1] = day
				}
			}
			if t.i < len(box)-1 {
				if check(pos{t.i + 1, t.j, t.k}, day) {
					queue = append(queue, pos{t.i + 1, t.j, t.k})
					days[t.i+1][t.j][t.k] = day
				}
			}
			if t.j < len(box[0])-1 {
				if check(pos{t.i, t.j + 1, t.k}, day) {
					queue = append(queue, pos{t.i, t.j + 1, t.k})
					days[t.i][t.j+1][t.k] = day
				}
			}
			if t.k < len(box[0][0])-1 {
				if check(pos{t.i, t.j, t.k + 1}, day) {
					queue = append(queue, pos{t.i, t.j, t.k + 1})
					days[t.i][t.j][t.k+1] = day
				}
			}
			queueSize--
		}
		day++
	}
}

func main() {
	maxDay := 0
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	scanner.Split(bufio.ScanWords)
	n, m, h := nextInt(), nextInt(), nextInt()
	box = make([][][]int, h)
	days = make([][][]int, h)
	for i := 0; i < h; i++ {
		box[i] = make([][]int, m)
		days[i] = make([][]int, m)
		for j := 0; j < m; j++ {
			box[i][j] = make([]int, n)
			days[i][j] = make([]int, n)
			for k := 0; k < n; k++ {
				scanner.Scan()
				box[i][j][k], _ = strconv.Atoi(scanner.Text())
				if box[i][j][k] == 1 || box[i][j][k] == -1 {
					days[i][j][k] = -1
				} else {
					days[i][j][k] = 0
				}
			}
		}
	}

	for i := 0; i < h; i++ {
		for j := 0; j < m; j++ {
			for k := 0; k < n; k++ {
				if box[i][j][k] == 1 {
					bfs(pos{i, j, k})
				}
			}
		}
	}

	for i := 0; i < h; i++ {
		for j := 0; j < m; j++ {
			for k := 0; k < n; k++ {
				if days[i][j][k] == 0 {
					fmt.Fprintln(w, "-1")
					return
				} else if days[i][j][k] == -1 {
					continue
				} else {
					maxDay = max(days[i][j][k], maxDay)
				}
			}
		}
	}

	fmt.Fprintln(w, maxDay)
}

func check(p pos, day int) bool {
	if days[p.i][p.j][p.k] == -1 {
		return false
	}
	if days[p.i][p.j][p.k] == 0 {
		return true
	}
	if days[p.i][p.j][p.k] > day {
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
