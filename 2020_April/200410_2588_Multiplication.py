# multiplication

n = int(input())
m = int(input())
multiplier = []
res = 0

for i in range(0, 3):
    multiplier.append(int(m / pow(10, 2 - i)))
    m %= pow(10, 2-i)

for i in range(2, -1, -1):
    temp = n * multiplier[i]
    print(temp)
    res += temp * pow(10, 2 - i)

print(res)