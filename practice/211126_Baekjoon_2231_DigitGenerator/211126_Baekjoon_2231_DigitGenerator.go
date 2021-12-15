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
	var g int
	if n > 18 {
		g = n - 9*numDigit(n)
	} else {
		g = 1
	}
	for g < n {
		if sumDigit(g) == n {
			fmt.Fprint(w, g)
			return
		} else {
			g++
		}
	}
	fmt.Fprint(w, 0)
}

func numDigit(n int) int {
	digits := 1
	for n >= 10 {
		n /= 10
		digits++
	}
	return digits
}

func sumDigit(n int) int {
	sum := n
	for n >= 10 {
		sum += n % 10
		n /= 10
	}
	sum += n
	return sum
}
