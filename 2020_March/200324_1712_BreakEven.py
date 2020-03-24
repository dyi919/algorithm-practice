# Find the break-even point of sales

import sys

fc, vc, p = map(int, sys.stdin.readline().split())

if vc < p:
    print(int(fc / (p - vc) + 1))
else:
    print(-1)