package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var (
	fb  map[int64]int64
	mod int64 = 1000000007
)

func getFibo(v int64) int64 {
	if ret, ok := fb[v]; ok {
		return ret
	}
	if v == 0 {
		return 0
	}
	if v < 3 {
		return 1
	}
	if v%2 == 0 {
		ret := (getFibo(v/2-1)*getFibo(v/2) + getFibo(v/2)*getFibo(v/2+1)) % mod
		fb[v] = ret
		return ret
	} else {
		ret := (getFibo(v/2-1)*getFibo(v/2+1) + getFibo(v/2)*getFibo(v/2+2)) % mod
		fb[v] = ret
		return ret
	}
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	scanner.Split(bufio.ScanWords)
	scanner.Scan()
	input, _ := strconv.Atoi(scanner.Text())
	n := int64(input)

	fb = make(map[int64]int64, 2)
	fb[0] = 0
	fb[1] = 1
	fb[2] = 1
	fb[3] = 2
	fmt.Fprint(w, getFibo(n))
}
