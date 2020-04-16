t = int(input())

for i in range(1, t + 1):
    a, b = [int(x) for x in input().split()]
    sum = a + b
    print("Case #%d: %d + %d = %d" % (i, a, b, sum))