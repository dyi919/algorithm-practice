package main

import (
	"bufio"
	"fmt"
	"os"
)

type Board [][]byte

func main() {
	var n, m, res int
	fmt.Scanln(&n, &m)
	min := 32
	scanner := bufio.NewScanner(os.Stdin)
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()

	b := make([][]byte, n)
	for i := 0; i < n; i++ {
		scanner.Scan()
		input := scanner.Bytes()
		line := make([]byte, len(input))
		copy(line, input)
		b[i] = line
	}
	for i := 0; i < len(b)-7; i++ {
		for j := 0; j < len(b[0])-7; j++ {
			temp := make([][]byte, 8)
			for k := 0; k < 8; k++ {
				temp[k] = make([]byte, 8)
				copy(temp[k], b[i+k][j:j+8])
			}
			res = countColor(temp)
			if res < min {
				min = res
			}
		}
	}
	fmt.Println(min)
}

func countColor(b Board) int {
	change := 0
	var match byte
	match = b[0][0]
	for i := 0; i < 8; i++ {
		for j := 0; j < 8; j++ {
			if b[i][j] != match {
				change++
			}
			if match == 87 {
				match = 66
			} else {
				match = 87
			}
		}
		if match == 87 {
			match = 66
		} else {
			match = 87
		}
	}
	if change > 32 {
		change = 64 - change
	}
	return change
}
