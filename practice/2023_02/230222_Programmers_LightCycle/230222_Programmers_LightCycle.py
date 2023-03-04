# https://school.programmers.co.kr/learn/courses/30/lessons/86052

def solution(grid):
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
    R, C = len(grid), len(grid[0])
    visited = [[[False] * 4 for _ in range(C)] for _ in range(R)]
    answer = []
    
    for k in range(4):
        for i in range(R):
            for j in range(C):
                if visited[i][j][k]: continue
                
                length = 0
                r, c, d = i, j, k

                while not visited[r][c][d]:
                    visited[r][c][d] = True
                    direction = grid[r][c]
                    
                    if direction == 'L':
                        d = 3 if d == 0 else d - 1
                    elif direction == 'R':
                        d = 0 if d == 3 else d + 1
                        
                    r += dr[d]
                    c += dc[d]
                    if r < 0: r = R - 1
                    if c < 0: c = C - 1
                    if r == R: r = 0
                    if c == C: c = 0
                    
                    length += 1
                        
                answer.append(length)
    
    return sorted(answer)