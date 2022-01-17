package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
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
	scanner.Scan()
	n, _ := strconv.Atoi(scanner.Text())
	paper = make([][]int, n)
	for i := 0; i < n; i++ {
		paper[i] = make([]int, n)
		for j := 0; j < n; j++ {
			scanner.Scan()
			paper[i][j], _ = strconv.Atoi(scanner.Text())
		}
	}
	fmt.Fprintln(w, cutPaper(-1, n, pos{0, 0}))
	fmt.Fprintln(w, cutPaper(0, n, pos{0, 0}))
	fmt.Fprintln(w, cutPaper(1, n, pos{0, 0}))
}

func cutPaper(num, len int, start pos) int {
	if len == 1 {
		if paper[start.y][start.x] == num {
			return 1
		} else {
			return 0
		}
	}

	isSame := true
	for i := start.y; i < start.y+len; i++ {
		for j := start.x; j < start.x+len; j++ {
			if paper[i][j] != num {
				isSame = false
				break
			}
		}
	}
	if isSame {
		return 1
	} else {
		len /= 3
		res := cutPaper(num, len, start)
		res += cutPaper(num, len, pos{start.x + len, start.y})
		res += cutPaper(num, len, pos{start.x + len*2, start.y})
		res += cutPaper(num, len, pos{start.x, start.y + len})
		res += cutPaper(num, len, pos{start.x + len, start.y + len})
		res += cutPaper(num, len, pos{start.x + len*2, start.y + len})
		res += cutPaper(num, len, pos{start.x, start.y + len*2})
		res += cutPaper(num, len, pos{start.x + len, start.y + len*2})
		res += cutPaper(num, len, pos{start.x + len*2, start.y + len*2})

		return res
	}

}
