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
	n, m := nextInt(), nextInt()
	q := make([]int, n+1)
	elems := make([]int, m)

	for i := 0; i < m; i++ {
		elems[i] = nextInt()
	}
	for i := 0; i < n+1; i++ {
		q[i] = i
	}

	current := 1
	ans := 0
	for i := 0; i < m; i++ {
		move := 0
		up, down := 0, 0
		if q[current] != elems[i] {
			for {
				move++
				if current+move > n {
					up = current - (n - move)
				} else {
					up = current + move
				}
				if current-move <= 0 {
					down = current + (n - move)
				} else {
					down = current - move
				}
				if q[up] == elems[i] || q[down] == elems[i] {
					if q[up] == elems[i] {
						current = up
					} else {
						current = down
					}
					break
				}
			}
			ans += move
		}
		if current == n {
			q = q[:current]
			current = 1
		} else {
			q = append(q[:current], q[current+1:]...)
		}
		n--
	}
	fmt.Fprint(w, ans)
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
