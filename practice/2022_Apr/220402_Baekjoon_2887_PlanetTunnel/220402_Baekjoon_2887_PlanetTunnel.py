# https://www.acmicpc.net/problem/2887

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

N = int(input())
planets = [[] for _ in range(N)]
edges = []
cycle = [x for x in range(N)]
count = 0
ans = 0

for i in range(N):
    planets[i] = [int(x) for x in stdin.readline().split()] + [i]

planets.sort(key=lambda x:x[0])
for i in range(1, N):
    edges.append((abs(planets[i-1][0] - planets[i][0]), planets[i-1][-1], planets[i][-1]))
planets.sort(key=lambda x:x[1])
for i in range(1, N):
    edges.append((abs(planets[i-1][1] - planets[i][1]), planets[i-1][-1], planets[i][-1]))
planets.sort(key=lambda x:x[2])
for i in range(1, N):
    edges.append((abs(planets[i-1][2] - planets[i][2]), planets[i-1][-1], planets[i][-1]))

edges.sort(key=lambda x:x[0])

for e in edges:
    if isSameParent(cycle, e[1], e[2]):
        continue
    unionParent(cycle, e[1], e[2])
    ans += e[0]
    count += 1
    if count == N-1:
        break
    
print(ans)