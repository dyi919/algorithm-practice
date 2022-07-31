# https://www.acmicpc.net/problem/10974

from sys import stdin
from itertools import permutations
input = stdin.readline

N = int(input())
permutation_list = list(permutations([i for i in range(1, N+1)], N))

for permutation in permutation_list:
    print(*permutation, sep=' ')