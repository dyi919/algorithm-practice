package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	scanner   = bufio.NewScanner(os.Stdin)
	w         = bufio.NewWriter(os.Stdout)
	inorder   []int
	postorder []int
	findIdx   []int
)

func main() {
	defer w.Flush()
	scanner.Split(bufio.ScanWords)
	n := nextInt()
	inorder = make([]int, n)
	postorder = make([]int, n)
	findIdx = make([]int, n+1)
	for i := 0; i < n; i++ {
		inorder[i] = nextInt()
		findIdx[inorder[i]] = i
	}
	for i := 0; i < n; i++ {
		postorder[i] = nextInt()
	}

	getPreorder(0, n-1, 0, n-1)
}

func getPreorder(ps, pe, is, ie int) {
	if ps > pe {
		return
	}
	root := postorder[pe]
	fmt.Fprintf(w, "%d ", root)

	rootIdx := findIdx[root]

	isLsub := is
	ieLsub := rootIdx - 1
	isRsub := rootIdx + 1
	ieRsub := ie

	psLsub := ps
	peLsub := ps + (ieLsub - isLsub)
	psRsub := ps + (ieLsub - isLsub) + 1
	peRsub := pe - 1

	getPreorder(psLsub, peLsub, isLsub, ieLsub)
	getPreorder(psRsub, peRsub, isRsub, ieRsub)
}

func nextInt() int {
	scanner.Scan()
	r := 0
	for _, c := range scanner.Bytes() {
		r *= 10
		r += int(c - '0')
	}
	return r
}
