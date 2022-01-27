package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var (
	scanner = bufio.NewScanner(os.Stdin)
	w       = bufio.NewWriter(os.Stdout)
)

func main() {
	defer w.Flush()
	scanner.Scan()
	n, _ := strconv.Atoi(scanner.Text())
	if n == 1 {
		fmt.Fprint(w, "0")
		return
	}
	sieve := make([]bool, n+1)
	var primes []int
	for i := 2; i <= n; i++ {
		if sieve[i] {
			continue
		}
		primes = append(primes, i)
		for j := i * i; j <= n; j += i {
			sieve[j] = true
		}
	}

	var start, end, sum, count int
	for {
		if sum < n {
			if end >= len(primes) {
				break
			}
			sum += primes[end]
			end++
			continue
		}
		if sum == n {
			count++
		}
		sum -= primes[start]
		start++
	}

	fmt.Fprintln(w, count)
}
