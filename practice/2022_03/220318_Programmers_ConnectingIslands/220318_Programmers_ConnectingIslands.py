# https://programmers.co.kr/learn/courses/30/lessons/42861

def getParent(set, x):
    if set[x] == x:
        return x
    else:
        return getParent(set, set[x])

def unionParent(set, a, b):
    a = getParent(set, a)
    b = getParent(set, b)
    if a < b:
        set[b] = a
    else:
        set[a] = b

def isSameParent(set, a, b):
    a = getParent(set, a)
    b = getParent(set, b)
    return True if a == b else False

def solution(n, costs):
    answer = 0
    cycle = [x for x in range(n)]
    costs.sort(key=lambda x:x[2])
    count = 0
    for c in costs:
        if isSameParent(cycle, c[0], c[1]):
            continue
        unionParent(cycle, c[0], c[1])
        answer += c[2]        
        count += 1
        if count == n-1:
            break
    return answer