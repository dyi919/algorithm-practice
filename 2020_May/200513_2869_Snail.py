import math

a, b, v = [int(x) for x in input().split()]

oneDay = a - b
total = math.ceil((v - b) / oneDay)


print(total)