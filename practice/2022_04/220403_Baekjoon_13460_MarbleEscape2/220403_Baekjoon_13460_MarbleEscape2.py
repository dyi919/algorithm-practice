# https://www.acmicpc.net/problem/13460

from sys import stdin
import collections

N, M = [int(x) for x in stdin.readline().split()]
board = [[] for _ in range(N)]
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
found = False
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
rx, ry, bx, by = -1, -1, -1, -1

def move(x, y, dx, dy):
    cnt = 0
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

for i in range(N):
    board[i] = stdin.readline().strip()
    for j in range(M):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j

q = collections.deque()
visited[rx][ry][bx][by] = True
q.append([rx, ry, bx, by, 1])

while q:
    rx, ry, bx, by, depth = q.popleft()
    for i in range(4):
        nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
        nbx, nby, bcnt = move(bx, by, dx[i], dy[i])
        if board[nbx][nby] != 'O': 
            if board[nrx][nry] == 'O':
                print(depth)
                found = True
                break

            if nrx == nbx and nry == nby:
                if rcnt > bcnt:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            if depth == 10: continue

            if not visited[nrx][nry][nbx][nby]:
                visited[rx][ry][bx][by] = True
                q.append((nrx, nry, nbx, nby, depth+1))

    if found: break

if not found: print(-1)
        
