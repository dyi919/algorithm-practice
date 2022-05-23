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
	n, m := nextInt(), nextInt()
	fiveCnt := powerCnt(n, 5) - powerCnt((n-m), 5) - powerCnt(m, 5)
	twoCnt := powerCnt(n, 2) - powerCnt((n-m), 2) - powerCnt(m, 2)
	fmt.Fprint(w, min(fiveCnt, twoCnt))
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func powerCnt(n, pow int) int {
	cnt := 0

	for n >= pow {
		cnt += n / pow
		n /= pow
	}

	return cnt
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
