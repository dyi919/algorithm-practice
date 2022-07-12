# https://www.acmicpc.net/problem/10775

from sys import stdin
input = stdin.readline

def find(x):
    if x == gates[x]:
        return gates[x]
    gates[x] = find(gates[x])
    return gates[x]

def union(a, b):
    a = find(a)
    b = find(b)
    gates[a] = b

G = int(input())
P = int(input())
gates = [i for i in range(G+1)]
ans = 0

for i in range(1, P+1):
    gate = int(input())

    docked = find(gate)
    if docked == 0:
        break
    else:
        union(docked, docked-1)
        ans += 1
    
print(ans)