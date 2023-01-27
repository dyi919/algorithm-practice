from collections import deque

def get_lines(rectangle):
    x_line, y_line = [], []
    
    for x1, y1, x2, y2 in rectangle:
        x_line.append([x1, x2, y1])
        x_line.append([x1, x2, y2])
        y_line.append([y1, y2, x1])
        y_line.append([y1, y2, x2])
    
    return [x_line, y_line]

def cut_lines(lines):
    x_line, y_line = lines
    cut_x_line, cut_y_line = [], []
    
    for i in range(len(x_line)):
        breakpoints = []
        x1, x2, y = x_line[i]
        min_x, max_x = min(x1, x2), max(x1, x2)
        
        for j in range(0, len(y_line), 2):
            y1, y2, x3 = y_line[j]
            _, _, x4 = y_line[j + 1]
            start_x, end_x = min(x3, x4), max(x3, x4)
            min_y, max_y = min(y1, y2), max(y1, y2)

            if start_x > max_x or end_x < min_x: continue
            if not min_y < y < max_y: continue
            breakpoints.append([start_x, end_x])
        
        if not breakpoints:
            cut_x_line.append([min_x, y, max_x, y])
            continue

        breakpoints.sort()

        prev = min_x
        for start, end in breakpoints:
            if start > max_x:
                start = max_x 
            if prev < start:
                cut_x_line.append([prev, y, start, y])
            prev = end
        if prev < max_x:
            cut_x_line.append([prev, y, max_x, y])
        
    for i in range(len(y_line)):
        breakpoints = []
        y1, y2, x = y_line[i]
        min_y, max_y = min(y1, y2), max(y1, y2)
        
        for j in range(0, len(x_line), 2):
            x1, x2, y3 = x_line[j]
            _, _, y4 = x_line[j + 1]
            start_y, end_y = min(y3, y4), max(y3, y4)
            min_x, max_x = min(x1, x2), max(x1, x2)

            if start_y > max_y or end_y < min_y: continue
            if not min_x < x < max_x: continue
            
            breakpoints.append([start_y, end_y])
        
        if not breakpoints:
            cut_y_line.append([x, min_y, x, max_y])
            continue

        breakpoints.sort()
        prev = min_y
        for start, end in breakpoints:
            if start > max_y:
                start = max_y 
            if prev < start:
                cut_y_line.append([x, prev, x, start])
            prev = end

        if prev < max_y:
            cut_y_line.append([x, prev, x, max_y])
    
    return cut_x_line, cut_y_line

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    visited = [[False] * 51 for _ in range(51)]
    graph = [[[] for _ in range(51)] for _ in range(51)]
    x_line, y_line = cut_lines(get_lines(rectangle))
    
    for from_x, from_y, to_x, to_y in x_line:
        for i in range(from_x, to_x):
            graph[i][from_y].append([i + 1, from_y])
            graph[i + 1][from_y].append([i, from_y])
    
    for from_x, from_y, to_x, to_y in y_line:
        for i in range(from_y, to_y):
            graph[from_x][i].append([from_x, i + 1])
            graph[from_x][i + 1].append([from_x, i])

    queue = deque()
    queue.append((characterX, characterY, 0)) 
    
    while queue:
        cur_x, cur_y, distance = queue.popleft()
        
        if cur_x == itemX and cur_y == itemY:
            return distance
        
        for next_x, next_y in graph[cur_x][cur_y]:
            if visited[next_x][next_y]: continue
            visited[next_x][next_y] = True
            queue.append((next_x, next_y, distance + 1))
    
    return answer