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
	if n != 1 {
		for n%2 == 0 {
			fmt.Fprintln(w, 2)
			n /= 2
		}
		for i := 3; i*i <= n; i += 2 {
			for n%i == 0 {
				fmt.Fprintln(w, i)
				n /= i
			}
		}
		if n > 2 {
			fmt.Fprintln(w, n)
		}
	}
}
