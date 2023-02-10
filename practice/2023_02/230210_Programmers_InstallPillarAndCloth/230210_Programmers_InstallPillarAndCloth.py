# https://school.programmers.co.kr/learn/courses/30/lessons/60061

def is_valid(blueprint, n):
    def has_pillar(x, y):
        if x < 0 or x > n or y < 0 or y > n: return False
        return blueprint[x][y] % 2 == 0
    
    def has_cloth(x, y):
        if x < 0 or x > n or y < 0 or y > n: return False
        return blueprint[x][y] > 0
    
    for x in range(n + 1):
        for y in range(n + 1):
            if has_pillar(x, y):
                # 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
                if not (y == 0 or (has_cloth(x - 1, y) or has_cloth(x, y)) or has_pillar(x, y - 1)):
                    return False
            if has_cloth(x, y):
                # 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
                if not ((has_pillar(x, y - 1) or has_pillar(x + 1, y - 1)) or (has_cloth(x - 1, y) and has_cloth(x + 1, y))):
                    return False
                        
    return True
                

def solution(n, build_frame):
    blueprint = [[-1] * (n + 1) for _ in range(n + 1)]
    answer = []
    
    for x, y, a, b in build_frame:
        temp = [row[:] for row in blueprint]
        
        if b == 0:
            temp[x][y] -= (a + 1)

        else:
            temp[x][y] += (a + 1)
        
        if is_valid(temp, n):
            blueprint = temp
            
    for x in range(n + 1):
        for y in range(n + 1):
            if -1 < blueprint[x][y] < 2:
                answer.append([x, y, blueprint[x][y]])
            elif blueprint[x][y] == 2:
                answer.append([x, y, 0])
                answer.append([x, y, 1])
    
    return answer