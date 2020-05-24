n = int(input())
arr = [0] * n * n
num = n

def star(n, x, y):
    if n == 1:
        arr[x * num + y] = 1
    else:
        div = n // 3
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1: continue
                star(div, x + div * i, y + div * j)

star(n, 0, 0)

for i in range(n):
    for j in range(n):
        if arr[i * num + j] == 1: print("*", end="")
        else: print(" ", end="")
    print()