t = int(input())

for _ in range(t):
    x, y = [int(x) for x in input().split()]
    dist = y - x
    speed = 0
    i = 0

    while i < dist:
        speed += 1
        i += speed * 2
    
    if dist > i - speed:
        print(speed * 2)
    else:
        print(speed * 2 - 1)