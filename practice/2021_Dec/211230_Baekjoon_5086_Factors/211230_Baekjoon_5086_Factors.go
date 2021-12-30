package main

import (
	"bufio"
	"fmt"
	"os"
)

var scanner = bufio.NewScanner(os.Stdin)

func main() {
	w := bufio.NewWriter(os.Stdout)
	scanner.Split(bufio.ScanWords)
	defer w.Flush()
	a, b := nextInt(), nextInt()
	for a != 0 && b != 0 {
		if a < b && b%a == 0 {
			fmt.Fprintln(w, "factor")
		} else if a%b == 0 {
			fmt.Fprintln(w, "multiple")
		} else {
			fmt.Fprintln(w, "neither")
		}
		a, b = nextInt(), nextInt()
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
