package main

import (
	"bufio"
	"fmt"
	"os"
)

var scanner = bufio.NewScanner(os.Stdin)

func main() {
	var a, s, nge []int
	var n int
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	scanner.Split(bufio.ScanWords)
	n = nextInt()
	a, nge = make([]int, n), make([]int, n)
	a[0] = nextInt()
	nge[0] = -1
	for i := 1; i < n; i++ {
		a[i] = nextInt()

		if a[i-1] < a[i] {
			nge[i-1] = a[i]
			for len(s) > 0 && a[s[len(s)-1]] < a[i] {
				nge[s[len(s)-1]] = a[i]
				s = s[:len(s)-1]
			}
		} else {
			s = append(s, i-1)
		}

		nge[i] = -1
	}
	
	for _, v := range nge {
		fmt.Fprintf(w, "%d ", v)
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
