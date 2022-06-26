# https://www.acmicpc.net/problem/1715

from sys import stdin
import heapq

input = stdin.readline
ans = 0
N = int(input())
cards = [int(input()) for _ in range(N)]
heapq.heapify(cards)

for _ in range(N-1):
    merge = heapq.heappop(cards) + heapq.heappop(cards)
    ans += merge
    heapq.heappush(cards, merge)
    
print(ans)