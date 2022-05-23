# https://www.acmicpc.net/problem/2268

from sys import stdin
from math import ceil, log2


def update_sum(node, start, end, idx, diff):
    if idx < start or idx > end:
        return
    tree_sum[node] += diff
    if start != end:
        mid = (start + end) // 2
        update_sum(node * 2, start, mid, idx, diff)
        update_sum(node * 2 + 1, mid + 1, end, idx, diff)


def query_sum(node, start, end, l, r):
    if r < start or l > end:
        return 0

    if l <= start and r >= end:
        return tree_sum[node]

    mid = (start + end) // 2
    return query_sum(node*2, start, mid, l, r) + query_sum(node*2+1, mid+1, end, l, r)


N, M = [int(x) for x in stdin.readline().split()]
ls = [0] * N
h = int(ceil(log2(N)))
tree_size = 1 << (h+1)
tree_sum = [0] * tree_size

for _ in range(M):
    a, b, c = [int(x) for x in stdin.readline().split()]
    if a == 1:
        diff = c - ls[b - 1]
        ls[b - 1] = c
        update_sum(1, 0, N - 1, b - 1, diff)
    else:
        if b > c:
            b, c = c, b
        print(query_sum(1, 0, N - 1, b - 1, c - 1))
