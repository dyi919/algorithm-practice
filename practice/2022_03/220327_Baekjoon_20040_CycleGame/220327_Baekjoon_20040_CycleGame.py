# https://www.acmicpc.net/problem/20040

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
cycle = [x for x in range(N)]
finished = False

for i in range(1, M+1):
    v1, v2 = [int(x) for x in stdin.readline().split()]
    if isSameParent(cycle, v1, v2):
        print(i)
        finished = True
        break
    unionParent(cycle, v1, v2)

if not finished:
    print("0")
