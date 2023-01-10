# https://school.programmers.co.kr/learn/courses/30/lessons/136797

def calc_weight(a, b):
    r_diff, c_diff = abs(a[0] - b[0]), abs(a[1] - b[1])
    weight = 3 * min(r_diff, c_diff) + 2 * abs(r_diff - c_diff)
    
    return weight
    
def solution(numbers):
    INF = 10 ** 9
    pos =  [[3, 1]]
    pos.extend([[i, j] for i in range(3) for j in range(3)])
    w = [[1 if i == j else calc_weight(pos[i], pos[j]) for j in range(10)] for i in range(10)]

    prev = [[INF] * 10 for _ in range(10)]
    prev[4][6] = 0
    prev[6][4] = 0
    
    for number in numbers:
        number = int(number)
        temp = [[INF] * 10 for _ in range(10)]
        
        for i in range(10):
            for j in range(10):
                if i == j: continue
                if prev[i][j] == INF: continue
                
                if i == number or j == number:
                    temp[i][j] = min(temp[i][j], prev[i][j] + 1)
                    continue
                    
                temp[i][number] = min(temp[i][number], prev[i][j] + w[j][number])
                temp[number][j] = min(temp[number][j], prev[i][j] + w[i][number])

        prev = temp
    
    return min(sum(prev, []))