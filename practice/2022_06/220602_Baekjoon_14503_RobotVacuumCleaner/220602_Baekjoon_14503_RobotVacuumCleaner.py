# https://www.acmicpc.net/problem/14503

from sys import stdin

# north, east, south, west
direction_row, direction_col = [-1, 0, 1, 0], [0, 1, 0, -1]  

N, M = [int(x) for x in stdin.readline().split()]

# direction - 0: north, 1: east, 2: south, 3: west
row, col, direction = [int(x) for x in stdin.readline().split()]

# board - 0: not cleaned, 1: wall, 2: cleaned
board = [[0] * M for _ in range(N)]
for i in range(N):
    board[i] = [int(x) for x in stdin.readline().split()]

cleaned_area = 0

while True:
    # if the area is not cleaned, clean the area
    if board[row][col] == 0:
        board[row][col] = 2
        cleaned_area += 1

    # turn left up to 4 times
    change_direction_count = 0
    while change_direction_count < 4:
        # north (0) -> west (3)
        if direction == 0:
            direction = 3
        else:
            direction -= 1
        
        # if the next location is not cleaned, go to that location, else turn left
        next_row, next_col = row + direction_row[direction], col + direction_col[direction]
        if board[next_row][next_col] == 0:
            break
        change_direction_count += 1
    
    # the cleaner turned left 4 times
    if change_direction_count == 4:
        prev_row, prev_col = row - direction_row[direction], col - direction_col[direction]
        # the wall is at the back - stop cleaning
        if board[prev_row][prev_col] == 1:
            break
        # go backward
        else:
            row, col = prev_row, prev_col
    # move to the next location
    else:
        row, col = next_row, next_col

print(cleaned_area)
