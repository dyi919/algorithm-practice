# https://school.programmers.co.kr/learn/courses/30/lessons/77485

def rotate_get_min(arr, q):
    x1, y1, x2, y2 = [v - 1 for v in q]

    new_arr = [a[:] for a in arr]
    min_val = 10001
    
    for x in range(x1, x2):
        new_arr[x][y1] = arr[x + 1][y1]
        new_arr[x + 1][y2] = arr[x][y2]
        min_val = min(min_val, new_arr[x + 1][y2], new_arr[x][y1])
    
    for y in range(y1, y2):
        new_arr[x1][y + 1] = arr[x1][y]
        new_arr[x2][y] = arr[x2][y + 1]
        min_val = min(min_val, new_arr[x1][y + 1], new_arr[x2][y])
    
    return new_arr, min_val

def solution(rows, columns, queries):
    answer = []
    arr = [[(i * columns) + j + 1 for j in range(columns)] for i in range(rows)]
    
    for q in queries:
        arr, min_val = rotate_get_min(arr, q)
        answer.append(min_val)
    
    return answer