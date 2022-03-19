# https://programmers.co.kr/learn/courses/30/lessons/43163

import collections
def solution(begin, target, words):
    if target not in words:
        return 0
    L = len(begin)
    d = collections.defaultdict()
    visited = collections.defaultdict()
    for word in words:
        visited[word] = -1
        for i in range(L):
            w = word[:i] + '_' + word[i+1:]
            if w in d:
                d[w].append(word)
            else:
                d[w] = [word]
    q = collections.deque([(begin, 0)])
    while q:
        current, count = q.popleft()
        if current != begin:
            if visited[current] != -1:
                continue
            visited[current] = count
            if current == target:
                break
        for i in range(L):
            w = current[:i] + '_' + current[i+1:]
            if w in d:
                for n in d[w]:
                    if visited[n] == -1:
                        q.append((n, count+1))
    return visited[target] if visited[target] != -1 else 0
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))