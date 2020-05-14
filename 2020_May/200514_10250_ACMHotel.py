import math

t = int(input())

for _ in range(t):
    h, w, n = [int(x) for x in input().split()]
    temp = n % h
    if temp == 0:
        roomNo = h * 100
    else: roomNo = (n % h) * 100
    roomNo += math.ceil(n / h)
    print(roomNo)