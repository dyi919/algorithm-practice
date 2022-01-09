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
	scanner.Scan()
	str := scanner.Text()
	for str != "." {
		s := []byte{}
		isBalanced := true
		for i := range str {
			if str[i] == byte('(') || str[i] == byte('[') {
				s = append(s, str[i])
			} else if str[i] == byte(')') {
				if len(s) == 0 {
					isBalanced = false
					break
				} 
				if s[len(s)-1] == byte('(') {
					s = s[:len(s)-1]
				} else {
					isBalanced = false
					break
				}
			} else if str[i] == byte(']') {
				if len(s) == 0 {
					isBalanced = false
					break
				} 
				if s[len(s)-1] == byte('[') {
					s = s[:len(s)-1]
				} else {
					isBalanced = false
					break
				}
			}
		}
		if len(s) == 0 && isBalanced {
			fmt.Fprintln(w, "yes")
		} else {
			fmt.Fprintln(w, "no")
		}
		scanner.Scan()
		str = scanner.Text()
	}
}

