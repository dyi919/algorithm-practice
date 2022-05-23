# https://www.acmicpc.net/problem/11505

from sys import stdin
from math import ceil,log2;
MOD = 1000000007

def init_prod(node, start, end):
    if start == end:
        tree_prod[node] = ls[start]
        return tree_prod[node]
    
    mid = (start + end) // 2
    tree_prod[node] = (init_prod(node*2, start, mid) * init_prod(node*2+1, mid+1, end)) % MOD
    return tree_prod[node]

def update_prod(node, start, end, idx, val):
    if idx < start or idx > end:
        return

    if start == end:
        tree_prod[node] = val
        return 
        
    mid = (start + end) // 2
    update_prod(node * 2, start, mid, idx, val)
    update_prod(node * 2 + 1, mid + 1, end, idx, val)
    tree_prod[node] = (tree_prod[node*2] * tree_prod[node*2+1]) % MOD

def query_prod(node, start, end, l, r):
    if r < start or l > end:
        return 1

    if l <= start and r >= end:
        return tree_prod[node]
    
    mid = (start + end) // 2
    return (query_prod(node*2, start, mid, l, r) * query_prod(node*2+1, mid+1, end, l, r)) % MOD

N, M, K = [int(x) for x in stdin.readline().split()]
ls = []
h = int(ceil(log2(N)))
tree_size = 1 << (h+1)
tree_prod = [0] * tree_size

for _ in range(N):
    ls.append(int(stdin.readline()))

init_prod(1, 0, N-1)

for _ in range(0, M + K):
    a, b, c = [int(x) for x in stdin.readline().split()]
    if a == 1:    
        update_prod(1, 0, N - 1, b - 1, c)
    else:
        print(query_prod(1, 0, N - 1, b - 1, c - 1))