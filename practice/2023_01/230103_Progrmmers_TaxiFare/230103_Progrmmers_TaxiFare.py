# https://school.programmers.co.kr/learn/courses/30/lessons/72413

from heapq import heappush, heappop

def solution(n, s, a, b, fares):
    INF = 10 ** 9
    graph = [[] for _ in range(n + 1)]
    
    for start, to, fare in fares:
        graph[start].append([to, fare])
        graph[to].append([start, fare])
    
    def dijkstra(start):
        costs = [INF] * (n + 1)
        costs[start] = 0
        pq = []
        heappush(pq, [costs[start], start])
        
        while pq:
            current_cost, current_place = heappop(pq)
            
            if costs[current_place] < current_cost:
                continue
            
            for next_place, next_cost in graph[current_place]:
                cost = current_cost + next_cost
                if cost < costs[next_place]:
                    costs[next_place] = cost
                    heappush(pq, [costs[next_place], next_place])
        
        return costs
    
    costs_s = dijkstra(s)
    costs_a = dijkstra(a)
    costs_b = dijkstra(b)
    
    sa = costs_s[a]
    sb = costs_s[b]
    
    answer = sa + sb
    
    for i in range(1, n + 1):
        si = costs_s[i]
        ai = costs_a[i]
        bi = costs_b[i]
        
        answer = min([answer, si + ai + bi])
    
    return answer