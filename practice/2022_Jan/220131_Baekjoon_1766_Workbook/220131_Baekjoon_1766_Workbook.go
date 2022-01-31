package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"os"
)

var (
	scanner  = bufio.NewScanner(os.Stdin)
	w        = bufio.NewWriter(os.Stdout)
	g        [][]int
	inDegree []int
	n, m     int
)

type Item struct {
	value    int // The value of the item; arbitrary.
	priority int // The priority of the item in the queue.
	// The index is needed by update and is maintained by the heap.Interface methods.
	index int // The index of the item in the heap.
}

// A PriorityQueue implements heap.Interface and holds Items.
type PriorityQueue []*Item

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {
	return pq[i].priority < pq[j].priority
}

func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].index = i
	pq[j].index = j
}

func (pq *PriorityQueue) Push(x interface{}) {
	n := len(*pq)
	item := x.(*Item)
	item.index = n
	*pq = append(*pq, item)
}

func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	item := old[n-1]
	old[n-1] = nil  // avoid memory leak
	item.index = -1 // for safety
	*pq = old[0 : n-1]
	return item
}

func main() {
	defer w.Flush()
	scanner.Split(bufio.ScanWords)
	n, m = nextInt(), nextInt()
	inDegree = make([]int, n+1)
	g = make([][]int, n+1)

	for i := 0; i < m; i++ {
		a, b := nextInt(), nextInt()
		g[a] = append(g[a], b)
		inDegree[b]++
	}
	topologicalSort()
}

func topologicalSort() {
	pq := make(PriorityQueue, 0, n)
	heap.Init(&pq)

	for i := 1; i <= n; i++ {
		if inDegree[i] == 0 {
			heap.Push(&pq, &Item{value: i, priority: i})
		}
	}

	for pq.Len() > 0 {
		v := heap.Pop(&pq).(*Item)
		current := v.value
		fmt.Fprintf(w, "%d ", current)
		for i := 0; i < len(g[current]); i++ {
			next := g[current][i]
			inDegree[next]--
			if inDegree[next] == 0 {
				heap.Push(&pq, &Item{value: next, priority: next})
			}
		}
	}
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
