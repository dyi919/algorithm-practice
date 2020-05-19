x, y, w, h = [int(x) for x in input().split()]

xdist = min(x, w - x)
ydist = min(y, h - y)
print(min(xdist, ydist))