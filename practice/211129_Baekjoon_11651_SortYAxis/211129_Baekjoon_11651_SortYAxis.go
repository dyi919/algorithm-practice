package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var n int
	r := bufio.NewReader(os.Stdin)
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	fmt.Fscan(r, &n)
	sCoords := make([][]int, n)
	for i := 0; i < n; i++ {
		s := make([]int, 2)
		fmt.Fscan(r, &s[0], &s[1])
		sCoords[i] = s
	}
	sCoords = mergeSort(sCoords)
	for _, s := range sCoords {
		fmt.Fprintln(w, s[0], s[1])
	}
}

func mergeSort(s [][]int) [][]int {
	if len(s) < 2 {
		return s
	}
	mid := len(s) / 2
	left := mergeSort(s[:mid])
	right := mergeSort(s[mid:])

	return merge(left, right)
}

func merge(left, right [][]int) [][]int {
	res := make([][]int, len(left)+len(right))
	for i := 0; len(left) > 0 || len(right) > 0; i++ {
		if len(left) > 0 && len(right) > 0 {
			if left[0][1] < right[0][1] {
				res[i] = left[0]
				left = left[1:]
			} else if left[0][1] > right[0][1] {
				res[i] = right[0]
				right = right[1:]
			} else if left[0][0] < right[0][0] {
				res[i] = left[0]
				left = left[1:]
			} else {
				res[i] = right[0]
				right = right[1:]
			}
		} else if len(left) > 0 {
			res[i] = left[0]
			left = left[1:]
		} else {
			res[i] = right[0]
			right = right[1:]
		}
	}
	return res
}
