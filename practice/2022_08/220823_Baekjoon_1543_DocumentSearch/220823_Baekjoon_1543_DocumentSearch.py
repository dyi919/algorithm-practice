# https://www.acmicpc.net/problem/1543

from sys import stdin
input = stdin.readline

doc = input().strip()
word = input().strip()
word_len = len(word)
ans = 0
idx = doc.find(word)

while idx != -1:
    ans += 1
    idx = doc.find(word, idx+word_len)

print(ans)