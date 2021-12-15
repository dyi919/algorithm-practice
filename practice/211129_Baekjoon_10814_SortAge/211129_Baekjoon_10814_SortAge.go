package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

type person struct {
	age  int
	name string
	idx  int
}

func main() {
	var n int
	r := bufio.NewReader(os.Stdin)
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	fmt.Fscan(r, &n)
	people := make([]person, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(r, &people[i].age, &people[i].name)
		people[i].idx = i
	}
	sort.Slice(people, func(i, j int) bool { return compare(people[i], people[j]) })
	for _, p := range people {
		fmt.Fprintln(w, p.age, p.name)
	}
}

func compare(p1, p2 person) bool {
	if p1.age != p2.age {
		return p1.age < p2.age
	}
	return p1.idx < p2.idx
}
