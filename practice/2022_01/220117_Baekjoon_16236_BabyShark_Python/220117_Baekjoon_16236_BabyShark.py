from sys import stdin


class Point:
    def __init__(self, i, j):
        self.i = i
        self.j = j


space = []
count = 0
size = 2
pos = Point(-1, -1)
ans = 0


def BFS():
    global ans
    distance = 0
    visited = [[False] * len(space) for _ in range(len(space))]
    queue = []
    candidates = []

    queue.append(pos)
    visited[pos.i][pos.j] = True

    while queue:
        queueSize = len(queue)
        while queueSize > 0:
            v = queue.pop(0)
            if space[v.i][v.j] > 0 and space[v.i][v.j] < size:
                candidates.append(Point(v.i, v.j))

            if v.i > 0:
                if visited[v.i-1][v.j] == False and space[v.i-1][v.j] <= size:
                    queue.append(Point(v.i-1, v.j))
                    visited[v.i-1][v.j] = True
            if v.j > 0:
                if visited[v.i][v.j-1] == False and space[v.i][v.j-1] <= size:
                    queue.append(Point(v.i, v.j-1))
                    visited[v.i][v.j-1] = True
            if v.i < len(space)-1:
                if visited[v.i+1][v.j] == False and space[v.i+1][v.j] <= size:
                    queue.append(Point(v.i+1, v.j))
                    visited[v.i+1][v.j] = True
            if v.j < len(space)-1:
                if visited[v.i][v.j+1] == False and space[v.i][v.j+1] <= size:
                    queue.append(Point(v.i, v.j+1))
                    visited[v.i][v.j+1] = True

            queueSize -= 1
        if len(candidates) > 0:
            choose = candidates[0]
            for i in range(1, len(candidates)):
                if candidates[i].i < choose.i or (candidates[i].i == choose.i and candidates[i].j < choose.j):
                    choose = candidates[i]
            eat(choose, distance)
            return True
        distance += 1
    return False


def eat(target, distance):
    global space, pos, size, ans, count

    space[pos.i][pos.j] = 0
    space[target.i][target.j] = 9
    ans += distance
    if size < 7:
        count += 1
        if count == size:
            size += 1
            count = 0
    pos.i, pos.j = target.i, target.j


n = int(input())
space = [[int(j) for j in stdin.readline().split()] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            pos.i, pos.j = i, j
            break

while True:
    if BFS() == False:
        print(ans)
        break
