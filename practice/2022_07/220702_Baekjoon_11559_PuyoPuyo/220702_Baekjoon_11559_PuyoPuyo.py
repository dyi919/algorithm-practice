# https://www.acmicpc.net/problem/11559

from sys import stdin
from collections import deque

input = stdin.readline
field = [input().strip() for _ in range(12)]
ans = 0
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
queue = deque()

def run():
    visited = [[False] * 6 for _ in range(12)]
    remove = []

    for i in range(12):
        for j in range(6):
            if not visited[i][j] and field[i][j] != '.':
                visited[i][j] = True
                queue.append((i, j))
                temp = [(i, j)]
                count = 1
                val = field[i][j]
                while queue:
                    x, y = queue.pop()
                    for k in range(4):
                        new_x, new_y = x+dx[k], y+dy[k]
                        if 0 <= new_x < 12 and 0 <= new_y < 6:
                            if not visited[new_x][new_y] and field[new_x][new_y] == val:
                                count += 1
                                visited[new_x][new_y] = True
                                queue.append((new_x, new_y))
                                temp += [(new_x, new_y)]
                if count >= 4:
                    remove += temp

    if remove:
        for i, j in remove:
            field[i] = field[i][:j] + '.' + field[i][j+1:]
        for i in range(6):
            j = 11
            while j >= 0:
                if field[j][i] != '.':
                    j -= 1
                else:
                    k = j-1
                    while k >= 0:
                        if field[k][i] != '.':
                            field[j] = field[j][:i] + field[k][i] + field[j][i+1:]
                            field[k] = field[k][:i] + '.' + field[k][i+1:]
                            break
                        k -= 1
                    j -= 1
        return True
    else:
        return False

while run():
    ans += 1
print(ans)