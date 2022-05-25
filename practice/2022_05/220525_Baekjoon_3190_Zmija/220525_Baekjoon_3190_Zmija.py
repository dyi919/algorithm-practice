# https://www.acmicpc.net/problem/3190

from sys import stdin
from collections import deque

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
N = int(input())
K = int(input())

apples = [[0] * 2 for _ in range(K)]

for i in range(K):
    apples[i] = [int(x) for x in stdin.readline().split()]

L = int(input())

instructions = deque()

for i in range(L):
    X, C = stdin.readline().split()
    instructions.append([int(X), C])

current_direction = 0  # 0 - Right, 1 - Down, 2 - Left, 3 - Up
time = 0
body = deque([[1, 1]])

while True:
    time += 1

    head = [body[-1][0] + dx[current_direction],
            body[-1][1] + dy[current_direction]]

    if head[0] < 1 or head[0] > N or head[1] < 1 or head[1] > N or head in body:
        break

    body.append(head)

    if head in apples:
        apples.remove(head)
    else:
        body.popleft()

    if instructions and time == instructions[0][0]:
        if instructions[0][1] == 'L':
            current_direction -= 1
            if current_direction < 0:
                current_direction = 3
        else:
            current_direction += 1
            if current_direction > 3:
                current_direction = 0
        instructions.popleft()

print(time)
