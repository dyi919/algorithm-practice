# https://www.acmicpc.net/problem/2294

from sys import stdin
from collections import deque
input = stdin.readline

n, k = map(int, input().split())
coins = list(filter(lambda x: x <= k, list(set([int(input()) for _ in range(n)]))))

queue = deque()
visited = [0] * (k+1)
found = False
ans = -1
for coin in coins:
    queue.append(coin)
    visited[coin] = 1

while queue:
    current_value = queue.popleft()
    for coin in coins:
        next_value = current_value + coin
        if next_value == k:
            found = True
            ans = visited[current_value] + 1
            break
        if next_value < k and visited[next_value] == 0:
            visited[next_value] = visited[current_value] + 1
            queue.append(next_value)
    if found:
        break

print(ans)