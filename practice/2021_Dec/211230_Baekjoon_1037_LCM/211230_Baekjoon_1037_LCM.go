package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

var scanner = bufio.NewScanner(os.Stdin)

func main() {
	w := bufio.NewWriter(os.Stdout)
	scanner.Split(bufio.ScanWords)
	defer w.Flush()
	n := nextInt()
	if n == 1 {
		s := nextInt()
		fmt.Fprint(w, s*s)
	} else {
		s := make([]int, n)
		for i := 0; i < n; i++ {
			s[i] = nextInt()
		}
		sort.Ints(s)
		fmt.Fprint(w, s[0]*s[n-1])
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
