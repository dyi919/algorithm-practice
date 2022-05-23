package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

var scanner = bufio.NewScanner(os.Stdin)

func main() {
	var total int
	w := bufio.NewWriter(os.Stdout)
	scanner.Split(bufio.ScanWords)
	defer w.Flush()
	n := nextInt()
	s := make([]int, n)
	for i := 0; i < n; i++ {
		s[i] = nextInt()
	}
	sort.Ints(s)
	for i := 0; i < n; i++ {
		total += s[i] * (n - i)
	}
	fmt.Fprint(w, total)
}

func nextInt() int {
	scanner.Scan()
	r, _ := strconv.Atoi(scanner.Text())
	return r
}
