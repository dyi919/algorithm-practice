# https://school.programmers.co.kr/learn/courses/30/lessons/87391

def move(p1, p2, steps, boundary):
    if p1 == 0 and steps < 0:
        p2 -= steps
    elif p2 == boundary and steps > 0:
        p1 -= steps
    else:
        p1 -= steps
        p2 -= steps
        
    p1 = max(p1, 0)
    p2 = min(p2, boundary)
    
    return p1, p2

def solution(n, m, x, y, queries):
    queries.reverse()
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    x1, x2, y1, y2 = x, x, y, y
        
    for d, steps in queries:
        x_move = dx[d] * steps
        y_move = dy[d] * steps

        if x_move:
            x1, x2 = move(x1, x2, x_move, n - 1)
            if x1 > x2: return 0
        else:
            y1, y2 = move(y1, y2, y_move, m - 1)
            if y1 > y2: return 0
    
    return (x2 - x1 + 1) * (y2 - y1 + 1)