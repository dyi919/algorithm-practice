# https://www.acmicpc.net/problem/15686

from sys import stdin
from itertools import combinations
input = stdin.readline

N, M = map(int, input().split())
house = []
chicken = []
distances = []

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j] == 1:
            house.append((i, j))
        elif line[j] == 2:
            chicken.append((i, j))

chicken_combination = list(combinations(chicken, M))

for c in chicken_combination:
    distance = 0
    for h in house:
        min_distance = 100
        for ci, cj in c:
            min_distance = min(min_distance, abs(h[0]-ci)+abs(h[1]-cj))
        distance += min_distance
    distances.append(distance)

print(sorted(distances)[0])