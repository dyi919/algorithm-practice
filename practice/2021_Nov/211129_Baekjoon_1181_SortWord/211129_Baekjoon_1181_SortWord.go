package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	var n int
	r := bufio.NewReader(os.Stdin)
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	fmt.Fscan(r, &n)
	words := make([]string, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(r, &words[i])
	}
	sort.Slice(words, func(i, j int) bool { return compare(words[i], words[j]) })
	prev := ""
	for _, s := range words {
		if s != prev {
			fmt.Fprintln(w, s)
			prev = s
		}
	}
}

func compare(s1, s2 string) bool {
	if len(s1) != len(s2) {
		return len(s1) < len(s2)
	}
	return s1 < s2
}
