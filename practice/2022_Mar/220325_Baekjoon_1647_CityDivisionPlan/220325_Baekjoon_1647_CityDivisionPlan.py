# https://www.acmicpc.net/problem/1647

from sys import stdin

def getParent(set, x):
    if set[x] == x:
        return x
    else:
        return getParent(set, set[x])

def unionParent(set, a, b):
    a = getParent(set, a)
    b = getParent(set, b)
    if a < b:
        set[b] = a
    else:
        set[a] = b

def isSameParent(set, a, b):
    a = getParent(set, a)
    b = getParent(set, b)
    return True if a == b else False

N, M = [int(x) for x in stdin.readline().split()]
edges = [[] for _ in range(M)]

for i in range(M):
    A, B, C = [int(x) for x in stdin.readline().split()]
    edges[i] = [A-1, B-1, C]

edges.sort(key=lambda x:x[2])
cycle = [x for x in range(N)]
ans = 0
count = 0

for e in edges:
    if isSameParent(cycle, e[0], e[1]):
        continue
    unionParent(cycle, e[0], e[1])
    ans += e[2]
    count += 1
    if count == N-2:
        break
    
print(ans)