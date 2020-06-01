n = int(input())
w = [0] * n
h = [0] * n
s = [1] * n
cnt = [0] * n

for i in range(n):
    w[i], h[i] = [int(x) for x in input().split()]

for i in range(n):
    for j in range(n):
        if i == j: continue
        if w[i] < w[j] and h[i] < h[j]:
            s[i] += 1

for score in s:
    print(score, end=" ")