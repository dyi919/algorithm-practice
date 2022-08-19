# https://www.acmicpc.net/problem/9934

from sys import stdin
from collections import deque
input = stdin.readline

K = int(input())
sequence = list(input().strip().split())
len_sequence = len(sequence)
queue = deque()
queue.append((len_sequence//2, len_sequence))

while queue:
    mid, length = queue.popleft()
    if length != len_sequence:
        print()
        len_sequence = length
    print(sequence[mid], end=" ")
    if length > 1:
        length //= 2
        left, right = mid - (length // 2 + 1), mid + (length // 2 + 1)
        queue.append((left, length))
        queue.append((right, length))
