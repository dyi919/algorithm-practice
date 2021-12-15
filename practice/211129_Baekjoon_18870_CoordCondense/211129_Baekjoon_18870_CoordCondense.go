package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

func main() {
	var n int
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanWords)
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	scanner.Scan()
	n, _ = strconv.Atoi(scanner.Text())

	var coords []int
	for i := 0; i < n; i++ {
		scanner.Scan()
		v, _ := strconv.Atoi(scanner.Text())
		coords = append(coords, v)
	}

	s := make([]int, len(coords))
	copy(s, coords)
	sort.Ints(s)
	s = removeDuplicate(s)
	for i := 0; i < len(coords); i++ {
		fmt.Fprint(w, sort.SearchInts(s, coords[i]), " ")
	}
}

func removeDuplicate(s []int) []int {
	allKeys := make(map[int]bool)
	list := []int{}
	for _, item := range s {
		if _, value := allKeys[item]; !value {
			allKeys[item] = true
			list = append(list, item)
		}
	}

	return list
}
