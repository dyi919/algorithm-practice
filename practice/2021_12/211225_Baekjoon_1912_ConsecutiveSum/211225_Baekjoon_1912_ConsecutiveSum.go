package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var scanner = bufio.NewScanner(os.Stdin)

func main() {
	var sum, largest int
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	scanner.Split(bufio.ScanWords)
	largest = -100000001
	n := nextInt()
	for i := 0; i < n; i++ {
		v := nextInt()
		if v < sum+v {
			sum += v
		} else {
			sum = v
		}
		if largest < sum {
			largest = sum
		}
	}
	fmt.Fprint(w, largest)
}

func nextInt() int {
	scanner.Scan()
	r, _ := strconv.Atoi(scanner.Text())
	return r
}
