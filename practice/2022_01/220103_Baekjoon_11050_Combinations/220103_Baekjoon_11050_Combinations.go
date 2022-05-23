package main

import (
	"bufio"
	"fmt"
	"os"
)

var scanner = bufio.NewScanner(os.Stdin)

func main() {
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	scanner.Split(bufio.ScanWords)
	a, b := nextInt(), nextInt()
	fmt.Fprint(w, fact(a)/(fact(b)*fact(a-b)))
}

func fact(a int) int {
	if a == 0 {
		return 1
	}
	res := 1
	for ; a > 1; a-- {
		res *= a
	}
	return res
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
