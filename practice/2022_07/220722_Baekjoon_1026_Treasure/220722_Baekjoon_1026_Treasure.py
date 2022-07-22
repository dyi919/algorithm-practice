# https://www.acmicpc.net/problem/1026

from sys import stdin
input = stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

print(sum([a * b for a, b in zip(A, B)]))