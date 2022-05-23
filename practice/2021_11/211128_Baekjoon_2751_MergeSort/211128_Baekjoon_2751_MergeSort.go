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
	s := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(r, &s[i])
	}
	s = mergeSort(s)
	for i := 0; i < n; i++ {
		fmt.Fprintln(w, s[i])
	}
}

func mergeSort(s []int) []int {
	if len(s) < 2 {
		return s
	}
	mid := len(s) / 2
	left := mergeSort(s[:mid])
	right := mergeSort(s[mid:])

	return merge(left, right)
}

func merge(left, right []int) []int {
	res := make([]int, len(left)+len(right))
	for i := 0; len(left) > 0 || len(right) > 0; i++ {
		if len(left) > 0 && len(right) > 0 {
			if left[0] < right[0] {
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
