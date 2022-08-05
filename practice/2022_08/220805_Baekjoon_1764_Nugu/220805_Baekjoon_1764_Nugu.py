# https://www.acmicpc.net/problem/1764

from sys import stdin
from collections import defaultdict
input = stdin.readline

N, M = map(int, input().split())
name_dict = defaultdict(int)
count = 0
ans_list = []

for _ in range(N+M):
    name = input().strip()
    if name_dict[name]:
        count += 1
        ans_list.append(name)
    else:
        name_dict[name] = 1

ans_list.sort()
print(count)
for name in ans_list:
    print(name)