# https://www.acmicpc.net/problem/2873

from sys import stdin
input = stdin.readline

R, C = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(R)]
moves = []
row_even = True if R % 2 == 0 else False
col_even = True if C % 2 == 0 else False

if row_even and not col_even:
    for i in range(C):
        if i % 2 == 0:
            moves += 'D'*(R-1)
        else:
            moves += 'U'*(R-1)
        moves += 'R'
    moves = moves[:-1]

elif not row_even:
    for i in range(R):
        if i % 2 == 0:
            moves += 'R'*(C-1)
        else:
            moves += 'L'*(C-1)
        moves += 'D'
    moves = moves[:-1]

else:
    min_val = 1001
    min_r, min_c = -1, -1
    for i in range(R):
        for j in range(C):
            if (i+j)%2 == 1 and min_val > land[i][j]:
                min_val = land[i][j]
                min_r, min_c = i, j
    
    new_r = min_r-1 if min_r%2 == 1 else min_r

    for i in range(new_r):
        if i % 2 == 0:
            moves += 'R'*(C-1)
        else:
            moves += 'L'*(C-1)
        moves += 'D'
    
    for i in range(min_c):
        if i % 2 == 0:
            moves += 'DR'
        else:
            moves += 'UR'
    
    for i in range(min_c, C-1):
        if i % 2 == 0:
            moves += 'RD'
        else:
            moves += 'RU'
    
    new_r = R-min_r-2 if min_r%2 == 0 else R-min_r-1

    for i in range(new_r):
        moves += 'D'
        if i % 2 == 0:
            moves += 'L'*(C-1)
        else:
            moves += 'R'*(C-1)
        
print(''.join(moves))