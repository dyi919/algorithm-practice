sides = [int(x) for x in input().split()]

while sides[0] != 0 and sides[1] != 0 and sides[2] != 0:
    sides.sort()

    if sides[0] * sides[0] + sides[1] * sides[1] == sides[2] * sides[2]:
        print("right")
    else: print("wrong")

    sides = [int(x) for x in input().split()]