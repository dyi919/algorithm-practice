# https://www.acmicpc.net/problem/14002

from sys import stdin
from bisect import bisect_left

N = int(input())
A = [int(x) for x in stdin.readline().split()]
min_of_len = [A[0]]
ans_len = 0
max_pos = [(0, A[0])]
ans = []

for i in range(1, N):
    if min_of_len[-1] < A[i]:
        min_of_len.append(A[i])
        ans_len += 1
        max_pos.append((ans_len, A[i]))
    else:
        pos = bisect_left(min_of_len, A[i])
        min_of_len[pos] = A[i]
        max_pos.append((pos, A[i]))

p = ans_len
ans_len += 1
for i in range(N-1, -1, -1):
    if max_pos[i][0] == p:
        ans.append(max_pos[i][1])
        p -= 1
ans.reverse()

print(ans_len)
print(*ans)