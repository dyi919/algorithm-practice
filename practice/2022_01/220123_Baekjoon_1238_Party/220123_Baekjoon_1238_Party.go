package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"math"
	"os"
)

var (
	scanner   = bufio.NewScanner(os.Stdin)
	w         = bufio.NewWriter(os.Stdout)
	goGraph   map[int]map[int]int
	backGraph map[int]map[int]int
	dist      [2][]int
	n, m, x   int
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
	n, m, x = nextInt(), nextInt(), nextInt()
	goGraph = make(map[int]map[int]int)
	backGraph = make(map[int]map[int]int)
	dist[0] = make([]int, n+1)
	dist[1] = make([]int, n+1)
	for i := 0; i <= n; i++ {
		dist[0][i], dist[1][i] = math.MaxInt32, math.MaxInt32
	}
	for i := 0; i < m; i++ {
		a, b, t := nextInt(), nextInt(), nextInt()
		if _, ok := goGraph[a]; ok {
			goGraph[a][b] = t
		} else {
			goGraph[a] = make(map[int]int)
			goGraph[a][b] = t
		}
		if _, ok := backGraph[b]; ok {
			backGraph[b][a] = t
		} else {
			backGraph[b] = make(map[int]int)
			backGraph[b][a] = t
		}
	}

	dijkstra(0)
	dijkstra(1)
	ans := 0
	for i := 1; i <= n; i++ {
		ans = max(ans, dist[0][i]+dist[1][i])
	}
	fmt.Fprintln(w, ans)
}

func dijkstra(mode int) {
	var graph map[int]map[int]int
	dist[mode][x] = 0
	if mode == 0 {
		graph = goGraph
	} else {
		graph = backGraph
	}

	pq := make(PriorityQueue, 0, n)
	heap.Init(&pq)
	heap.Push(&pq, &Item{value: x, priority: 0})

	for pq.Len() > 0 {
		v := heap.Pop(&pq).(*Item)
		min := v.priority
		current := v.value

		if min > dist[mode][current] {
			continue
		}

		for key, elem := range graph[current] {
			next := key
			nextDist := elem + min

			if nextDist < dist[mode][next] {
				dist[mode][next] = nextDist
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
