# https://www.acmicpc.net/problem/1043

from operator import truth
from sys import stdin

def getParent(set, x):
    if set[x] == x:
        return x
    else:
        return getParent(set, set[x])

def unionParent(set, a, b, truth_people):
    a = getParent(set, a)
    b = getParent(set, b)

    if a in truth_people and b in truth_people:
        return
    
    if a in truth_people:
        set[b] = a
    elif b in truth_people:
        set[a] = b
    else:
        if a < b:
            set[b] = a
        else:
            set[a] = b

N, M = [int(x) for x in stdin.readline().split()]
truth_people = [int(x) for x in stdin.readline().split()][1:]

parent = list(range(N+1))
parties = []
for _ in range(M):
    party = [int(x) for x in stdin.readline().split()]
    party_len, party_people = party[0], party[1:]
    for i in range(party_len-1):
        unionParent(parent, party_people[i], party_people[i+1], truth_people)
    parties.append(party_people)

ans = 0
for party in parties:
    for i in range(len(party)):
        if getParent(parent, party[i]) in truth_people:
            break
    else:
        ans += 1

print(ans)