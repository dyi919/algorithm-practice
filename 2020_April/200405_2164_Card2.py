# n cards, discard 1 card and put the first card behind the last card until 1 card remains

import collections

n = int(input())
q = collections.deque()
ans = 1

for i in range(1, n + 1):
    q.append(i)

while len(q) > 1:
    q.popleft()
    ans = q.popleft()
    q.append(ans)

print(ans)