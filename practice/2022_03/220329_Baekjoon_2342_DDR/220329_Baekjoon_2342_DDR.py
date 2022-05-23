from sys import stdin, maxsize

moves = {
    0: [0, 2, 2, 2, 2],
    1: [0, 1, 3, 4, 3],
    2: [0, 3, 1, 3, 4],
    3: [0, 4, 3, 1, 3],
    4: [0, 3, 4, 3, 1]
}
steps = [int(x) for x in stdin.readline().split()]
steps = steps[:-1]
L = len(steps)
cache = [[[maxsize] * 5 for _ in range(5)] for _ in range(L+1)]
cache[0][0][0] = 0
for n in range(L):
    s = steps[n]
    for i in range(5):
        for j in range(5):
            if cache[n][i][j] != maxsize:
                cache[n+1][s][j] = min(cache[n][i][j] +
                                       moves[i][s], cache[n+1][s][j])
                cache[n+1][i][s] = min(cache[n][i][j] +
                                       moves[j][s], cache[n+1][i][s])

print(min(cache[L][i][j] for i in range(5) for j in range(5)))
