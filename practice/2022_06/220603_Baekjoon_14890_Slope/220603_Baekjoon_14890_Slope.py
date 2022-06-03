# https://www.acmicpc.net/problem/14890

from sys import stdin


def pos(now):
    for j in range(1, n):
        if abs(now[j] - now[j - 1]) > 1:
            return False
        if now[j] < now[j - 1]:
            for k in range(l):
                if j + k >= n or used[j + k] or now[j] != now[j + k]:
                    return False
                if now[j] == now[j + k]:
                    used[j + k] = True
        elif now[j] > now[j - 1]:
            for k in range(l):
                if j - k - 1 < 0 or now[j - 1] != now[j - k - 1] or used[j - k - 1]:
                    return False
                if now[j - 1] == now[j - k - 1]:
                    used[j - k - 1] = True
    return True


n, l = [int(x) for x in stdin.readline().split()]
board = [list(map(int, stdin.readline().split())) for _ in range(n)]
result = 0

for i in range(n):
    used = [False for _ in range(n)]
    if pos(board[i]):
        result += 1

for i in range(n):
    used = [False for _ in range(n)]
    if pos([board[j][i] for j in range(n)]):
        result += 1

print(result)


"""

from sys import stdin

ans = 0
N, L = [int(x) for x in stdin.readline().split()]
board = [[0] * N for _ in range(N)]

for i in range(N):
    board[i] = [int(x) for x in stdin.readline().split()]


def check_possible():
    ans = 0

    for i in range(N):
        has_slope = [False] * N
        possible = True
        for j in range(1, N):
            if abs(board[i][j] - board[i][j-1]) > 1:
                possible = False
                break
            elif board[i][j] == board[i][j-1]:
                continue
            else:
                up = False  # slope going upward
                height = 0
                if board[i][j] > board[i][j-1]:
                    height = board[i][j-1]
                    up = True
                else:
                    j -= 1
                    height = board[i][j+1]
                for k in range(1, L+1):
                    if up:
                        k = -k
                    if j+k < N and board[i][j+k] == height and not has_slope[j+k]:
                        has_slope[j+k] = True
                    else:
                        possible = False
                        break
        if possible:
            ans += 1
    return ans


ans = check_possible()
for i in range(N):
    for j in range(i+1, N):
        board[i][j], board[j][i] = board[j][i], board[i][j]
ans += check_possible()

print(ans)
"""
