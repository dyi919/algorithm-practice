from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def get_shape(table, N):
    shapes = []
    visited = [[False] * N for _ in range(N)]
    q = deque()

    for i in range(N):
        for j in range(N):
            if table[i][j] == 0 or visited[i][j]:
                continue

            visited[i][j] = True
            q.append((i, j))
            shape = [(i, j)]

            while q:
                x, y = q.popleft()

                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < N and 0 <= ny < N and table[nx][ny] == 1 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        shape.append((nx, ny))
                        q.append((nx, ny))
            shapes.append(normalize(shape))

    return shapes

def fill(board, shapes, N):
    answer = 0
    visited = [[False] * N for _ in range(N)]
    q = deque()

    for i in range(N):
        for j in range(N):
            if board[i][j] == 1 or visited[i][j]:
                continue

            temp_visited = [x[:] for x in visited]
            temp_visited[i][j] = True
            q.append((i, j))
            space = [(i, j)]
            idx = -1

            while q:
                x, y = q.popleft()

                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0 and not temp_visited[nx][ny]:
                        temp_visited[nx][ny] = True
                        space.append((nx, ny))
                        q.append((nx, ny))

            normalized = normalize(space)
            area = len(normalized)
            match = False

            for k in range(len(shapes)):
                if len(shapes[k]) != area: 
                    continue

                current_shape = shapes[k]

                for _ in range(4):
                    current_shape = rotate(current_shape)

                    if sorted(current_shape) == sorted(normalized):
                        match = True
                        answer += area
                        break

                if match:
                    idx = k
                    shapes.pop(idx)
                    visited = temp_visited
                    break

    return answer

def normalize(shape):
    new_shape = []
    x_diff, y_diff = shape[0]
    
    for x, y in shape:
        new_shape.append((x - x_diff, y - y_diff))
        
    return new_shape

def rotate(shape):
    new_shape = []
    
    for x, y in shape:
        new_shape.append((y, -x))
        
    return new_shape

def solution(game_board, table):
    N = len(table)
    
    shapes = get_shape(table, N)
    return fill(game_board, shapes, N)