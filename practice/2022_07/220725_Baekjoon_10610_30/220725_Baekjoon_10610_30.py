# https://www.acmicpc.net/problem/10610

from sys import stdin
input = stdin.readline

N = list(input().strip())

if sum(list(map(int, N))) % 3 != 0:
    print(-1)
else:
    N.sort(reverse=True)
    if N[-1] != '0':
        print(-1)
    else:
        print(''.join(N))