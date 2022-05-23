package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

var (
	scanner = bufio.NewScanner(os.Stdin)
	w       = bufio.NewWriter(os.Stdout)
	nums    map[int]int
	keys    []int
	n, m    int
)

func main() {
	defer w.Flush()
	scanner.Split(bufio.ScanWords)
	n, m = nextInt(), nextInt()
	nums = make(map[int]int)
	for i := 0; i < n; i++ {
		num := nextInt()
		if _, ok := nums[num]; ok {
			nums[num]++
		} else {
			nums[num] = 1
		}
	}

	keys = make([]int, 0, len(nums))
	for k := range nums {
		keys = append(keys, k)
	}
	sort.Ints(keys)

	printComb([]int{})
}

func printComb(comb []int) {
	if len(comb) == m {
		for i := 0; i < m; i++ {
			fmt.Fprintf(w, "%d ", comb[i])
		}
		fmt.Fprintln(w)
		return
	}
	for i := 0; i < len(keys); i++ {
		if nums[keys[i]] > 0 {
			comb = append(comb, keys[i])
			nums[keys[i]]--
			printComb(comb)
			comb = comb[:len(comb)-1]
			nums[keys[i]]++
		}
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
