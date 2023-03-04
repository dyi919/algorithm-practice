# https://school.programmers.co.kr/learn/courses/30/lessons/87377

def normalize(p, x_min, y_min):
    return (p[0] - x_min, p[1] - y_min)

def solution(line):
    N = len(line)
    stars = []
    
    for i in range(N - 1):
        A, B, E = line[i]
        for j in range(i + 1, N):
            C, D, F = line[j]
            divisor = A * D - B * C
            if divisor == 0: continue
            
            x, x_mod = divmod((B * F - E * D), divisor)
            y, y_mod = divmod((E * C - A * F), divisor)
            
            if x_mod == 0 and y_mod == 0:
                stars.append((x, -y))
    
    x_sorted = sorted(stars)
    y_sorted = sorted(stars, key=lambda x: x[1])

    x_min = x_sorted[0][0]
    x_max = x_sorted[-1][0] - x_min
    y_min = y_sorted[0][1] 
    y_max = y_sorted[-1][1] - y_min
    
    normalized_stars = list(map(lambda s: normalize(s, x_min, y_min), stars))
    
    board = [['.'] * (x_max + 1) for _ in range(y_max + 1)]

    for x, y in normalized_stars:
        board[y][x] = '*'
    
    return list(map(''.join, board))