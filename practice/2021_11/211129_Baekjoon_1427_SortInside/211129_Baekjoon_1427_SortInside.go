package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	var n int
	r := bufio.NewReader(os.Stdin)
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	fmt.Fscan(r, &n)
	s := strconv.Itoa(n)
	res := strings.Split(s, "")
	sort.Sort(sort.Reverse(sort.StringSlice(res)))
	fmt.Fprint(w, strings.Join(res, ""))
}
