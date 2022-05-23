from sys import stdin

N = int(input())
ls = [list(map(str, stdin.readline().split())) for _ in range(N)]
ans = sorted(ls, key=lambda x: int(x[0]))
for a in ans:
    print(a[0], a[1])
