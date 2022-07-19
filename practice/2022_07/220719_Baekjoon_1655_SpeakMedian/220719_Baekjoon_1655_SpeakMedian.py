from sys import stdin
import heapq
input = stdin.readline

N = int(input())
left_heap = []
right_heap = []
left_heap_len, right_heap_len = 0, 0

len_nums = 0

for _ in range(N):
    num = int(input())
    if left_heap_len == right_heap_len:
        heapq.heappush(left_heap, (-num, num))
        left_heap_len += 1
    else:
        heapq.heappush(right_heap, (num, num))
        right_heap_len += 1
    
    if right_heap and left_heap[0][1] > right_heap[0][0]:
        smaller = heapq.heappop(right_heap)[0]
        larger = heapq.heappop(left_heap)[1]
        heapq.heappush(left_heap, (-smaller, smaller))
        heapq.heappush(right_heap, (larger, larger))
    
    print(left_heap[0][1])