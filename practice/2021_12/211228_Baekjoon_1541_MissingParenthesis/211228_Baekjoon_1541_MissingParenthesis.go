package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var scanner = bufio.NewScanner(os.Stdin)

func main() {
	var sum int
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	scanner.Scan()

	s := strings.Split(scanner.Text(), "-")
	for i := 0; i < len(s); i++ {
		nums := strings.Split(s[i], "+")
		if i == 0 {
			for _, num := range nums {
				v, _ := strconv.Atoi(num)
				sum += v
			}
		} else {
			for _, num := range nums {
				v, _ := strconv.Atoi(num)
				sum -= v
			}
		}
	}
	fmt.Fprint(w, sum)
}
