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
	t := nextInt()
	for i := 0; i < t; i++ {
		n := nextInt()
		categories := make(map[string]int)
		ans := 1
		for j := 0; j < n; j++ {
			scanner.Scan()
			scanner.Scan()
			category := scanner.Text()
			if cnt, ok := categories[category]; ok {
				categories[category] = cnt + 1
			} else {
				categories[category] = 2
			}
		}
		for _, v := range categories {
			ans *= v
		}
		fmt.Fprintln(w, ans-1)
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
