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
	queue := make([]int, 0, 2000000)
	n := nextInt()
	for i := 0; i < n; i++ {
		scanner.Scan()
		switch command := scanner.Text(); command {
		case "push":
			v := nextInt()
			queue = append(queue, v)
		case "pop":
			if len(queue) == 0 {
				fmt.Fprintln(w, "-1")
			} else {
				fmt.Fprintln(w, queue[0])
				queue = queue[1:]
			}
		case "size":
			fmt.Fprintln(w, len(queue))
		case "empty":
			if len(queue) == 0 {
				fmt.Fprintln(w, "1")
			} else {
				fmt.Fprintln(w, "0")
			}
		case "front":
			if len(queue) == 0 {
				fmt.Fprintln(w, "-1")
			} else {
				fmt.Fprintln(w, queue[0])
			}
		case "back":
			if len(queue) == 0 {
				fmt.Fprintln(w, "-1")
			} else {
				fmt.Fprintln(w, queue[len(queue)-1])
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
