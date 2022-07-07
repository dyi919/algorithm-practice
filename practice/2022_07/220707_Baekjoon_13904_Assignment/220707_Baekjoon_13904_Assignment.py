# https://www.acmicpc.net/problem/13904

from sys import stdin

input = stdin.readline
N = int(input())
assignments = []
scores = [0] * (1001)

for _ in range(N):
    assignments.append((list(map(int, input().split()))))

assignments = sorted(assignments, key=lambda x: x[1], reverse=True)
for due, score in assignments:
    for i in range(due, 0, -1):
        if scores[i] == 0 :
            scores[i] = score
            break

print(sum(scores))