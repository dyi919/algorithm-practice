# https://www.acmicpc.net/problem/1275

from sys import stdin
from math import ceil, log2


def init_sum(node, start, end):
    if start == end:
        tree_sum[node] = ls[start]
        return tree_sum[node]

    mid = (start + end) // 2
    tree_sum[node] = init_sum(node*2, start, mid) + \
        init_sum(node*2+1, mid+1, end)
    return tree_sum[node]


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


N, Q = [int(x) for x in stdin.readline().split()]
ls = [int(x) for x in stdin.readline().split()]
h = int(ceil(log2(N)))
tree_size = 1 << (h+1)
tree_sum = [0] * tree_size

init_sum(1, 0, N-1)

for _ in range(Q):
    x, y, a, b = [int(x) for x in stdin.readline().split()]
    if x > y:
        x, y = y, x
    print(query_sum(1, 0, N - 1, x - 1, y - 1))
    diff = b - ls[a - 1]
    ls[a - 1] = b
    update_sum(1, 0, N - 1, a - 1, diff)
