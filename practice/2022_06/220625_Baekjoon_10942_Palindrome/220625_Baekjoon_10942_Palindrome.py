# https://www.acmicpc.net/problem/10942

from sys import stdin

N = int(input())
numbers = [int(x) for x in stdin.readline().split()]
cache = [[-1] * N for _ in range(N)]

def check_palindrome(S, E):
    if S == E:
        return 1
    if S+1 == E:
        return 1 if numbers[S] == numbers[E] else 0
    if cache[S][E] != -1:
        return cache[S][E]
    else:
        if numbers[S] == numbers[E]:
            cache[S][E] = check_palindrome(S+1, E-1)
        else:
            cache[S][E] = 0
        return cache[S][E]

M = int(input())
for _ in range(M):
    S, E = [int(x) for x in stdin.readline().split()]
    print(check_palindrome(S-1, E-1))