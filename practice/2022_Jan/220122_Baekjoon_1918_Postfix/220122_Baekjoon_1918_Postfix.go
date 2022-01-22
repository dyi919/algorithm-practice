package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	scanner  = bufio.NewScanner(os.Stdin)
	w        = bufio.NewWriter(os.Stdout)
	equation []byte
	result   []byte
	stack    []byte
)

func main() {
	defer w.Flush()
	scanner.Scan()
	equation = []byte(scanner.Text())
	stack = make([]byte, 0, len(equation))

	convert()
}

func convert() {
	top := -1
	for i := 0; i < len(equation); i++ {
		if equation[i] >= 'A' && equation[i] <= 'Z' {
			fmt.Fprintf(w, "%c", equation[i])
		} else if equation[i] == '(' {
			stack = append(stack, equation[i])
			top++
		} else if equation[i] == ')' {
			for stack[top] != '(' {
				fmt.Fprintf(w, "%c", stack[top])
				stack = stack[:top]
				top--
			}
			stack = stack[:top]
			top--
		} else {
			if top == -1 || stack[top] == '(' {
				stack = append(stack, equation[i])
				top++
			} else {
				if compare(equation[i], stack[top]) > 0 {
					stack = append(stack, equation[i])
					top++
				} else {
					for top > -1 && isOperator(stack[top]) && compare(equation[i], stack[top]) < 1 {
						fmt.Fprintf(w, "%c", stack[top])
						stack = stack[:top]
						top--
					}
					stack = append(stack, equation[i])
					top++
				}
			}
		}
	}
	for top > -1 {
		fmt.Fprintf(w, "%c", stack[top])
		stack = stack[:top]
		top--
	}
}

func isOperator(a byte) bool {
	if a == '+' || a == '-' || a == '*' || a == '/' {
		return true
	}
	return false
}

func compare(a, b byte) int { // return 1 if a > b, 0 if a == b, -1 if a < b
	if a == '*' || a == '/' {
		if b == '+' || b == '-' {
			return 1
		}
		return 0
	} else {
		if b == '+' || b == '-' {
			return 0
		}
		return -1
	}
}
