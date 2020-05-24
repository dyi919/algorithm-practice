t = int(input())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = [int(x) for x in input().split()]
    dist = pow((x1 - x2) ** 2 + (y1 - y2) ** 2, 0.5)
    R = max(r1, r2)
    r = min(r1, r2)
    if R == r and dist == 0: print(-1)
    elif dist == R + r: print(1)
    elif dist + r == R: print(1)
    elif dist > R + r: print(0)
    elif R != r and dist + r < R: print(0)
    else: print(2)