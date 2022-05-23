# https://www.acmicpc.net/problem/9252

s1 = input()
s2 = input()
l1, l2 = len(s1), len(s2)
cache = [[[-1, ""] for _ in range(l2+1)] for _ in range(l1+1)]
ans = []

for i in range(l1+1):
    for j in range(l2+1):
        if i == 0 or j == 0:
            cache[i][j] = [0, ""]
        elif s1[i-1] == s2[j-1]:
            cache[i][j] = cache[i-1][j-1][0]+1, cache[i-1][j-1][1]+s1[i-1]
        else:
            cache[i][j] = cache[i-1][j] if cache[i-1][j][0] > cache[i][j-1][0] else cache[i][j-1]

l, substr = cache[l1][l2]
print(l)
if l > 0:
    print(substr)
