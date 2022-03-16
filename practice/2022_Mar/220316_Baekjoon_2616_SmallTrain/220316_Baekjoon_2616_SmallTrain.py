from sys import stdin

N = int(input())
T = [int(x) for x in stdin.readline().split()]
L = int(input())

smallT = [0] * N
smallT[0] = T[0]
for i in range(1, L):
    smallT[i] = smallT[i-1]+T[i]
for i in range(L, N):
    smallT[i] = smallT[i-1] - T[i-L] + T[i]

cache = [[0] * N for _ in range(4)]

for i in range(1, 4):
    for j in range(i*L-1, N):
        cache[i][j] = max(cache[i][j-1], cache[i-1][j-L] + smallT[j])

print(cache[3][N-1])

