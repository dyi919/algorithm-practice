package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

var (
	scanner    = bufio.NewScanner(os.Stdin)
	w          = bufio.NewWriter(os.Stdout)
	nums, comb []int
	picked     []bool
	n, m       int
)

func main() {
	defer w.Flush()
	scanner.Split(bufio.ScanWords)
	n, m = nextInt(), nextInt()
	nums = make([]int, n)
	comb = make([]int, m)
	picked = make([]bool, n)

	for i := 0; i < n; i++ {
		nums[i] = nextInt()
	}
	sort.Ints(nums)

	pick(0)
}

func pick(pos int) {
	if pos == m {
		printComb()
		return
	}
	for i := 0; i < n; i++ {
		if picked[i] {
			continue
		} else {
			comb[pos] = nums[i]
			picked[i] = true
			pick(pos + 1)
			picked[i] = false
		}
	}
}

func printComb() {
	for i := 0; i < m; i++ {
		fmt.Fprintf(w, "%d ", comb[i])
	}
	fmt.Fprintln(w)
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
