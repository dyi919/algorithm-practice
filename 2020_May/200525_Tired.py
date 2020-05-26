n = int(input())
a = [0, 0] * n

for _ in range(n):
    a.append([int(x) for x in input().split()])