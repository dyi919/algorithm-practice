from sys import stdin, maxsize

moves = {
    0: [(), (1, 2), (2, 2), (3, 2), (4, 2)],
    1: [(), (1, 1), (2, 3), (3, 4), (4, 3)],
    2: [(), (1, 3), (2, 1), (3, 3), (4, 4)],
    3: [(), (1, 4), (2, 3), (3, 1), (4, 3)],
    4: [(), (1, 3), (2, 4), (3, 3), (4, 1)]
}
steps = [int(x) for x in stdin.readline().split()]
steps = steps[:-1]
L = len(steps)
cache = [[[maxsize] * 5 for _ in range(5)] for _ in range(L+1)]
cache[0][0][0] = 0
cache[1][steps[0]][0] = moves[0][steps[0]][1]
cache[1][0][steps[0]] = moves[0][steps[0]][1]
for n in range(1, L):
    s = steps[n]
    for i in range(5):
        for j in range(5):
            if cache[n][i][j] != maxsize:
                cache[n+1][s][j] = min(cache[n][i][j] + moves[i][steps[]])

for i in range(1, L+1):
    move_from1, move_from2 = cache[i-1][0], cache[i-1][1]
    move_to = steps[i-1]
    l1 = moves[move_from1[0]][move_to]
    l2 = moves[move_from2[0]][move_to]
    if move_from1[2] + l1[1] < move_from2[2] + l2[1]:
        cache[i][0] = [move_to, move_from1[1], move_from1[2]+l1[1]]
    else:
        cache[i][0] = [move_to, move_from2[1], move_from2[2]+l2[1]]
    
    r1 = moves[move_from1[1]][move_to]
    r2 = moves[move_from2[1]][move_to]
    if move_from1[2] + r1[1] < move_from2[2] + r2[1]:
        cache[i][1] = [move_from1[0], move_to, move_from1[2]+r1[1]]
    else:
        cache[i][1] = [move_from2[0], move_to, move_from2[2]+r2[1]]
print(cache)
print(min(cache[L][0][2], cache[L][1][2]))
