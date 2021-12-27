package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

var scanner = bufio.NewScanner(os.Stdin)
var max int

func main() {
	var endTime, cnt int
	w := bufio.NewWriter(os.Stdout)
	scanner.Split(bufio.ScanWords)
	defer w.Flush()
	n := nextInt()
	s := make([][2]int, n)
	for i := 0; i < n; i++ {
		s[i][0], s[i][1] = nextInt(), nextInt()
	}
	sort.Slice(s, func(i, j int) bool {
		if s[i][1] == s[j][1] {
			return s[i][0] < s[j][0]
		}
		return s[i][1] < s[j][1]
	})
	endTime = s[0][1]
	cnt++
	for i := 1; i < n; i++ {
		if endTime <= s[i][0] {
			cnt++
			endTime = s[i][1]
		}
	}
	fmt.Fprint(w, cnt)
}

func nextInt() int {
	scanner.Scan()
	r, _ := strconv.Atoi(scanner.Text())
	return r
}
