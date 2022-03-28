# https://www.acmicpc.net/problem/4386

from sys import stdin
import collections, math

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

N = int(input())
cycle = [x for x in range(N)]
vdict = collections.defaultdict()
edges = []

for i in range(N):
    x, y = [float(x) for x in stdin.readline().split()]
    vdict[i] = (x, y)
    for j in range(i):
        edges.append([j, i, math.dist(vdict[i], vdict[j])])

edges.sort(key=lambda x:x[2])
count = 0
ans = 0

for e in edges:
    if isSameParent(cycle, e[0], e[1]):
        continue
    unionParent(cycle, e[0], e[1])
    ans += e[2]
    count += 1
    if count == N-1:
        break
    
print(ans)