# Blackjack

import sys

n, m = map(int, sys.stdin.readline().split())
cards = [int(x) for x in sys.stdin.readline().split()]
maxVal = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        sum = cards[i] + cards[j]
        for k in range(j + 1, n):
            temp = sum + cards[k]
            if m - temp >= 0 and maxVal < temp: maxVal = temp
            if maxVal == m: break
        if maxVal == m: break
    if maxVal == m: break

print(maxVal)
