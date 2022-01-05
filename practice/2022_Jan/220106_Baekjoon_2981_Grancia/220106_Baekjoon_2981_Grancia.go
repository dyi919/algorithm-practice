package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
)

var scanner = bufio.NewScanner(os.Stdin)

func main() {
	var s [100]int
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	scanner.Split(bufio.ScanWords)
	n := nextInt()
	s[0], s[1] = nextInt(), nextInt()
	g := diff(s[0], s[1])
	for i := 2; i < n; i++ {
		s[i] = nextInt()
		d := diff(s[i-1], s[i])
		g = gcd(g, d)
	}
	res := getFactors(g)
	for i := range res {
		fmt.Fprintf(w, "%d ", res[i])
	}
}

func getFactors(n int) []int {
	var result []int
	for i := 1; i <= int(math.Sqrt(float64(n))); i++ {
		if n%i == 0 {
			if n/i == i {
				result = append(result, i)
			} else {
				result = append(result, i, n/i)
			}
		}
	}
	sort.Ints(result)
	return result[1:]
}

func diff(a, b int) int {
	if a > b {
		return a - b
	}
	return b - a
}

func gcd(a, b int) int {
	if a < b {
		a, b = b, a
	}
	for b != 0 {
		a, b = b, a%b
	}
	return a
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
