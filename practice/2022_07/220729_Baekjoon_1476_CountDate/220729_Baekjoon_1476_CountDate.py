# https://www.acmicpc.net/problem/1476

from sys import stdin
input = stdin.readline

E, S, M = map(int, input().split())
if E == 15: 
    E = 0
    ans = 15
else: 
    ans = E

if S == 28:
    S = 0

if M == 19:
    M = 0

while ans % 15 != E or ans % 28 != S or ans % 19 != M:
    ans += 15

print(ans)