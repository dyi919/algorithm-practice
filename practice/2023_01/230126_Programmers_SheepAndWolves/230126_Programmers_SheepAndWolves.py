# https://school.programmers.co.kr/learn/courses/30/lessons/92343

def solution(info, edges):
    N = len(info)
    answer = 0
    tree = [[] for _ in range(N)]
    
    for a, b in edges:
        tree[a].append(b)
        
    def dfs(node, sheep, wolves, next_list):
        nonlocal answer
        if info[node] == 0:
            sheep += 1
        else:
            wolves += 1
            
        if sheep <= wolves: return
        if sheep > answer: answer = sheep
        
        next_list.extend(tree[node])
        
        for i in range(len(next_list)):
            dfs(next_list[i], sheep, wolves, next_list[:i] + next_list[i + 1:])
            
    dfs(0, 0, 0, [])
    
    return answer