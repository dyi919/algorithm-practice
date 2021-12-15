package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type pos struct {
	y int
	x int
}

var (
	s   [][]int
	row [][]bool
	col [][]bool
	sqr [][]bool
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()

	s = make([][]int, 9)
	row = make([][]bool, 9)
	col = make([][]bool, 9)
	sqr = make([][]bool, 9)
	for i := range s {
		s[i] = make([]int, 9)
		row[i] = make([]bool, 10)
		col[i] = make([]bool, 10)
		sqr[i] = make([]bool, 10)
	}
	for i := 0; i < 9; i++ {
		scanner.Scan()
		s[i] = numbers(scanner.Text())
	}
	for i := 0; i < 9; i++ {
		for j := 0; j < 9; j++ {
			v := s[i][j]
			row[i][v] = true
			col[j][v] = true
			sqr[getSRange(i, j)][v] = true
		}
	}

	z := getZeroes(s)
	n := len(z)
	solve(n)

}

func solve(n int) bool {
	if n == 0 {
		printBoard(s)
		return true
	}
	for i := 0; i < 9; i++ {
		for j := 0; j < 9; j++ {
			if s[i][j] == 0 {
				for k := 1; k < 10; k++ {
					if !row[i][k] && !col[j][k] && !sqr[getSRange(i, j)][k] {
						s[i][j] = k
						row[i][k] = true
						col[j][k] = true
						sqr[getSRange(i, j)][k] = true
						if solve(n - 1) {
							return true
						}
						s[i][j] = 0
						row[i][k] = false
						col[j][k] = false
						sqr[getSRange(i, j)][k] = false
					}
				}
				return false
			}
		}
	}

	return false
}

func printBoard(s [][]int) {
	for i := 0; i < 9; i++ {
		for j := 0; j < 9; j++ {
			fmt.Printf("%d ", s[i][j])
		}
		fmt.Println()
	}
}

func getSRange(i, j int) int {
	return i/3*3 + j/3
}

func getZeroes(s [][]int) []pos {
	var p []pos
	for i := 0; i < 9; i++ {
		for j := 0; j < 9; j++ {
			if s[i][j] == 0 {
				p = append(p, pos{i, j})
			}
		}
	}
	return p
}

func numbers(s string) []int {
	var n []int
	for _, f := range strings.Fields(s) {
		i, err := strconv.Atoi(f)
		if err == nil {
			n = append(n, i)
		}
	}
	return n
}
