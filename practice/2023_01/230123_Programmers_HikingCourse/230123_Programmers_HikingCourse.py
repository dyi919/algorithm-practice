from heapq import heappush, heappop
INF = 10 ** 9

def solution(n, paths, gates, summits):
    summits_set = set(summits)
    graph = [[] for _ in range(n + 1)]
    intensity_cache = [INF] * (n + 1)
    pq = []
    
    for i, j, w in paths:
        graph[i].append([j, w])
        graph[j].append([i, w])
    
    for gate in gates:
        intensity_cache[gate] = 0
        heappush(pq, [0, gate])

    while pq:
        intensity, cur = heappop(pq)

        if cur in summits_set or intensity > intensity_cache[cur]: 
            continue

        for nxt, nxt_intensity in graph[cur]:
            nxt_intensity = max(intensity, nxt_intensity)

            if nxt_intensity < intensity_cache[nxt]:
                intensity_cache[nxt] = nxt_intensity
                heappush(pq, [nxt_intensity, nxt])
    
    summits.sort(key=lambda x: (intensity_cache[x], x))
    return [summits[0], intensity_cache[summits[0]]]