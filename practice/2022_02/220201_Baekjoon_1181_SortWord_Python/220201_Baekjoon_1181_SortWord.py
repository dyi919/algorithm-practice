from sys import stdin

N = int(input())
ls = [stdin.readline().strip() for _ in range(N)]
ls = list(dict.fromkeys(ls))
ans = sorted(ls, key=lambda x: (len(x), x))
for a in ans:
    print(a)
