apt = [[0] * 15 for _ in range(15)]

for i in range(15):
    apt[0][i] = i + 1
    apt[i][0] = 1

for i in range(1, 15):
    for j in range(1 , 15):
        apt[i][j] = apt[i - 1][j] + apt[i][j - 1]


t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())

    print(apt[k][n - 1])