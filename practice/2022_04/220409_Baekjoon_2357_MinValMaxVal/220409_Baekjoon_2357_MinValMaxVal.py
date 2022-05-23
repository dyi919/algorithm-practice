# https://www.acmicpc.net/problem/10868

from sys import stdin, maxsize
from math import ceil,log2;
INT_MAX = maxsize

def init_min(node, start, end):
    if start == end:
        tree_min[node] = ls[start]
        return tree_min[node]
    
    mid = (start + end) // 2
    tree_min[node] = min(init_min(node*2, start, mid), init_min(node*2+1, mid+1, end))
    return tree_min[node]

def init_max(node, start, end):
    if start == end:
        tree_max[node] = ls[start]
        return tree_max[node]
    
    mid = (start + end) // 2
    tree_max[node] = max(init_max(node*2, start, mid), init_max(node*2+1, mid+1, end))
    return tree_max[node]

def query_min(node, start, end, l, r):
    if r < start or l > end:
        return INT_MAX

    if l <= start and r >= end:
        return tree_min[node]
    
    mid = (start + end) // 2
    return min(query_min(node*2, start, mid, l, r), query_min(node*2+1, mid+1, end, l, r))

def query_max(node, start, end, l, r):
    if r < start or l > end:
        return 0

    if l <= start and r >= end:
        return tree_max[node]
    
    mid = (start + end) // 2
    return max(query_max(node*2, start, mid, l, r), query_max(node*2+1, mid+1, end, l, r))

N, M = [int(x) for x in stdin.readline().split()]
ls = []
h = int(ceil(log2(N)))
tree_size = 1 << (h+1)
tree_min = [0] * tree_size
tree_max = [0] * tree_size

for _ in range(N):
    ls.append(int(stdin.readline()))

init_min(1, 0, N-1)
init_max(1, 0, N-1)

for _ in range(M):
    a, b = [int(x) for x in stdin.readline().split()]

    print(query_min(1, 0, N-1, a-1, b-1), query_max(1, 0, N-1, a-1, b-1))