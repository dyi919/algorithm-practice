# https://school.programmers.co.kr/learn/courses/30/lessons/86971

from collections import defaultdict, deque

def solution(n, wires):
    min_diff = 101
    
    for i in range(len(wires)):
        cut_wires = wires[:i] + wires[i+1:]
        
        wire_dict = defaultdict(list)
        for wire_from, wire_to in cut_wires:
            wire_dict[wire_from].append(wire_to)
            wire_dict[wire_to].append(wire_from)
        
        visited = [False] * (n+1)
        visited[cut_wires[0][0]] = True
        queue = deque([cut_wires[0][0]])
        total = 1
        while queue:
            cur = queue.popleft()
            for neighbor in wire_dict[cur]:
                if not visited[neighbor]:
                    total += 1
                    visited[neighbor] = True
                    queue.append(neighbor)

        diff = abs(n - total - total)
        min_diff = min(diff, min_diff)
        
    return min_diff