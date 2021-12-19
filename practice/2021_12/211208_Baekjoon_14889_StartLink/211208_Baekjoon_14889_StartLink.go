package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

var diff = math.MaxInt32

func main() {
	var n int
	scanner := bufio.NewScanner(os.Stdin)
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	scanner.Scan()
	n, _ = strconv.Atoi(scanner.Text())

	s := make([][]int, n)
	for i := range s {
		s[i] = make([]int, n)
	}
	for i := 0; i < n; i++ {
		scanner.Scan()
		s[i] = numbers(scanner.Text())
	}
	a := make([]int, n/2-1)
	check := make([]int, n+1)

	dfs(s, a, check, 0, 1, n)
	fmt.Println(diff)
}

func dfs(s [][]int, a, check []int, pos, prev, n int) {
	if pos == len(a) {
		temp := []int{0}
		diff = min(diff, getDiff(s, append(temp, a...)))
	} else {
		for i := prev; i < n; i++ {
			if check[i] == 0 {
				a[pos] = i
				check[i] = 1
				dfs(s, a, check, pos+1, i, n)
				check[i] = 0
			}
		}
	}
}

func getDiff(s [][]int, team1 []int) int {
	sum1, sum2 := 0, 0
	team2 := make([]int, len(team1))
	j := 0
	for i := 0; i < len(team1)*2 && j < len(team2); i++ {
		if !contains(team1, i) {
			team2[j] = i
			j++
		}
	}

	for _, i := range team1 {
		for _, j := range team1 {

			sum1 += s[i][j]
		}
	}
	for _, i := range team2 {
		for _, j := range team2 {
			sum2 += s[i][j]
		}
	}

	diff := sum1 - sum2
	if diff > 0 {
		return diff
	}
	return 0 - diff
}

func contains(s []int, e int) bool {
	for _, a := range s {
		if a == e {
			return true
		}
	}
	return false
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func numbers(s string) []int {
	var n []int
	for _, f := range strings.Fields(s) {
		i, err := strconv.Atoi(f)
		if err == nil {
			n = append(n, i)
		}
	}
	return n
}
