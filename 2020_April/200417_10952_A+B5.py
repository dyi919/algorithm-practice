# prints A + B until inputs 0 0

a, b = [int(x) for x in input().split()]
res = a + b

while res != 0:
    print(res)
    a, b = [int(x) for x in input().split()]
    res = a + b