package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

var scanner = bufio.NewScanner(os.Stdin)

const MaxBuf int = 400000

func main() {
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	scanner.Split(bufio.ScanWords)
	scanner.Buffer(make([]byte, 0, MaxBuf), MaxBuf)
	t := nextInt()

	for k := 0; k < t; k++ {
		scanner.Scan()
		cmd := scanner.Text()
		nextInt()
		scanner.Scan()
		sliceStr := scanner.Text()
		s := []string{}
		if sliceStr != "[]" {
			s = strings.Split(sliceStr[1:len(sliceStr)-1], ",")
		}
		reversed := false
		isError := false

		for i := 0; i < len(cmd); i++ {
			if cmd[i] == 'R' {
				reversed = !reversed
			} else {
				if len(s) == 0 {
					isError = true
					break
				} else if !reversed {
					s = s[1:]
				} else {
					s = s[:len(s)-1]
				}
			}
		}

		if isError {
			fmt.Fprintln(w, "error")
		} else {
			if reversed && len(s) > 1 {
				for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
					s[i], s[j] = s[j], s[i]
				}
			}
			fmt.Fprintln(w, "["+strings.Join(s, ",")+"]")
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
