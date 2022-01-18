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
}

var scanner = bufio.NewScanner(os.Stdin)
var s [][]byte
var visitedHuman [][]bool
var visitedCow [][]bool

func bfs(startPos pos, isCow bool) int { //iscow: r=g
	var vmode [][]bool
	color := []byte{}
	queue := make([]pos, 0)

	queue = append(queue, startPos)

	if isCow {
		if s[startPos.i][startPos.j] == 'R' || s[startPos.i][startPos.j] == 'G' {
			color = append(color, 'R', 'G')
		} else {
			color = append(color, 'B')
		}
		vmode = visitedCow
	} else {
		color = append(color, s[startPos.i][startPos.j])
		vmode = visitedHuman
	}
	vmode[startPos.i][startPos.j] = true

	for len(queue) > 0 {
		v := queue[0]
		queue = queue[1:]
		if v.i > 0 {
			if vmode[v.i-1][v.j] == false && contains(color, s[v.i-1][v.j]) {
				queue = append(queue, pos{v.i - 1, v.j})
				vmode[v.i-1][v.j] = true
			}
		}
		if v.j > 0 {
			if vmode[v.i][v.j-1] == false && contains(color, s[v.i][v.j-1]) {
				queue = append(queue, pos{v.i, v.j - 1})
				vmode[v.i][v.j-1] = true
			}
		}
		if v.i < len(s)-1 {
			if vmode[v.i+1][v.j] == false && contains(color, s[v.i+1][v.j]) {
				queue = append(queue, pos{v.i + 1, v.j})
				vmode[v.i+1][v.j] = true
			}
		}
		if v.j < len(s)-1 {
			if vmode[v.i][v.j+1] == false && contains(color, s[v.i][v.j+1]) {
				queue = append(queue, pos{v.i, v.j + 1})
				vmode[v.i][v.j+1] = true
			}
		}

	}

	return 1
}

func main() {
	hCount, cCount := 0, 0
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	scanner.Split(bufio.ScanLines)
	scanner.Scan()
	n, _ := strconv.Atoi(scanner.Text())
	s = make([][]byte, n)
	for i := 0; i < n; i++ {
		scanner.Scan()
		s[i] = []byte(scanner.Text())
	}
	count := 0
	for i := 0; i < n; i++ {
		if s[0][i] == 'R' {
			count++
		}
	}
	visitedHuman = make([][]bool, n)
	visitedCow = make([][]bool, n)
	for i := 0; i < n; i++ {
		visitedHuman[i] = make([]bool, n)
		visitedCow[i] = make([]bool, n)
		for j := 0; j < n; j++ {
			visitedHuman[i][j] = false
			visitedCow[i][j] = false
		}
	}

	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if !visitedHuman[i][j] {
				hCount += bfs(pos{i, j}, false)
			}
			if !visitedCow[i][j] {
				cCount += bfs(pos{i, j}, true)
			}
		}
	}

	fmt.Fprint(w, hCount, cCount)
}

func contains(colors []byte, color byte) bool {
	for _, c := range colors {
		if color == c {
			return true
		}
	}
	return false
}
