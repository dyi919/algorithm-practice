# https://www.acmicpc.net/problem/10828

from sys import stdin
from collections import deque
input = stdin.readline

N = int(input())
stack = deque()
stack_size = 0

for _ in range(N):
    command = list(input().strip().split())
      
    if command[0] == "push":
        stack.append(command[1])
        stack_size += 1
    elif command[0] == "pop":
        if stack:
            print(stack.pop())
            stack_size -= 1
        else:
            print(-1)
    elif command[0] == "size":
        print(stack_size)
    elif command[0] == "empty":
        print(0 if stack_size > 0 else 1)
    elif command[0] == "top":
        print(stack[-1] if stack else -1)
    