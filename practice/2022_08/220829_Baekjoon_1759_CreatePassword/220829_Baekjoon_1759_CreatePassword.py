# https://www.acmicpc.net/problem/1759

from sys import stdin
from itertools import combinations
input = stdin.readline

def isVowel(c):
    return 1 if c in 'aeiou' else 0

L, C = map(int, input().split())
alphabets = sorted(list(input().strip().split()))
candidates = list(combinations(alphabets, L))

for candidate in candidates:
    num_vowels = 0
    for c in candidate:
        num_vowels += isVowel(c)
    if 1 <= num_vowels < L-1:
        print(''.join(candidate))