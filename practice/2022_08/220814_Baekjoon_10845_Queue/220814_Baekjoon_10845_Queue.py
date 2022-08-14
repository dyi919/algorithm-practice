# https://www.acmicpc.net/problem/10845

from sys import stdin
from collections import deque
input = stdin.readline

N = int(input())
queue = deque()
queue_size = 0

for _ in range(N):
    command = list(input().strip().split())
      
    if command[0] == "push":
        queue.append(command[1])
        queue_size += 1
    elif command[0] == "pop":
        if queue:
            print(queue.popleft())
            queue_size -= 1
        else:
            print(-1)
    elif command[0] == "size":
        print(queue_size)
    elif command[0] == "empty":
        print(0 if queue_size > 0 else 1)
    elif command[0] == "front":
        print(queue[0] if queue else -1)
    elif command[0] == "back":
        print(queue[-1] if queue else -1)