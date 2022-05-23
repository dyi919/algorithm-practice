package main

import (
	"bufio"
	"fmt"
	"os"
)

type elem struct {
	index      int
	importance int
}

var scanner = bufio.NewScanner(os.Stdin)

func main() {
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	scanner.Split(bufio.ScanWords)
	t := nextInt()
	for k := 0; k < t; k++ {
		n, pos := nextInt(), nextInt()
		ans := 0
		q := make([]elem, n)

		for i := 0; i < n; i++ {
			q[i].index = i
			q[i].importance = nextInt()
		}

		for len(q) > 0 {
			idx := 0
			for i := 1; i < len(q); i++ {
				if q[0].importance < q[i].importance {
					idx = i
					break
				}
			}
			if idx == 0 {
				ans++
				if q[idx].index == pos {
					fmt.Fprintln(w, ans)
					break
				}
				q = q[1:]
			} else {
				q = append(q[1:], q[0])
			}
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
