package main

import (
	"bufio"
	"fmt"
	"os"
)

type pos struct {
	x int
	y int
}

var scanner = bufio.NewScanner(os.Stdin)

var paper [][]int

func main() {
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	scanner.Split(bufio.ScanWords)
	n := nextInt()
	paper = make([][]int, n)
	for i := 0; i < n; i++ {
		paper[i] = make([]int, n)
		for j := 0; j < n; j++ {
			paper[i][j] = nextInt()
		}
	}
	fmt.Fprintln(w, cutPaper(0, n, pos{0, 0}))
	fmt.Fprintln(w, cutPaper(1, n, pos{0, 0}))
}

func cutPaper(color, len int, start pos) int {
	if len == 1 {
		if paper[start.y][start.x] == color {
			return 1
		} else {
			return 0
		}
	}

	isColor := true
	for i := start.y; i < start.y+len; i++ {
		for j := start.x; j < start.x+len; j++ {
			if paper[i][j] != color {
				isColor = false
				break
			}
		}
	}
	if isColor {
		return 1
	} else {
		len /= 2
		return cutPaper(color, len, start) + cutPaper(color, len, pos{start.x + len, start.y}) + cutPaper(color, len, pos{start.x, start.y + len}) + cutPaper(color, len, pos{start.x + len, start.y + len})
	}

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
