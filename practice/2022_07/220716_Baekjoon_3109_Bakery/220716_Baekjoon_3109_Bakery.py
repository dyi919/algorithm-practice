# https://www.acmicpc.net/problem/3109

from sys import stdin
input = stdin.readline

dr = [-1, 0, 1]
R, C = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
conncted = False
ans = 0

def dfs(r, c):
    global ans
    visited[r][c] = True
    if c == C-1:
        ans += 1
        return True
    for i in range(3):
        nr = r+dr[i]
        if 0 <= nr < R and grid[nr][c+1] == '.' and not visited[nr][c+1]:
            if dfs(nr, c+1):
                return True
    return False

for r in range(R):
    dfs(r, 0)

print(ans)
