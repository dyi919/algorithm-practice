package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"math"
	"os"
)

var (
	scanner          = bufio.NewScanner(os.Stdin)
	w                = bufio.NewWriter(os.Stdout)
	graph            map[int]map[int]int
	dist, prev, path []int
	n, m, s, e, cnt  int
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
	graph = make(map[int]map[int]int)

	dist = make([]int, n+1)
	prev = make([]int, n+1)

	for i := 0; i <= n; i++ {
		dist[i] = math.MaxInt32
	}
	for i := 0; i < m; i++ {
		a, b, c := nextInt(), nextInt(), nextInt()
		if _, ok := graph[a]; ok {
			if _, ok := graph[a][b]; ok {
				if graph[a][b] > c {
					graph[a][b] = c
				}
			} else {
				graph[a][b] = c
			}
		} else {
			graph[a] = make(map[int]int)
			graph[a][b] = c
		}
	}
	s, e = nextInt(), nextInt()

	dijkstra()

	fmt.Fprintln(w, dist[e])
	fmt.Fprintln(w, cnt)
	for i := 0; i < len(path); i++ {
		fmt.Fprintf(w, "%d ", path[i])
	}
}

func dijkstra() {
	cnt = 0
	dist[s] = 0
	prev[s] = -1

	pq := make(PriorityQueue, 0, n)
	heap.Init(&pq)
	heap.Push(&pq, &Item{value: s, priority: 0})

	for pq.Len() > 0 {
		v := heap.Pop(&pq).(*Item)
		min := v.priority
		current := v.value

		if min > dist[current] {
			continue
		}

		if current == e {
			if prev[current] != -1 || s == current {
				for current != -1 {
					path = append([]int{current}, path...)
					current = prev[current]
					cnt++
				}
				return
			}
		}

		for key, elem := range graph[current] {
			next := key
			nextDist := elem + min

			if nextDist < dist[next] {
				dist[next] = nextDist
				prev[next] = current
				heap.Push(&pq, &Item{value: key, priority: nextDist})
			}
		}
	}
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
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
