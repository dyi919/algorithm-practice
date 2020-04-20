n = int(input())

i = 0

while i < n:
    for j in range(0, n):
        if i - j > 0:
            print(" ", end = "")
        else: print("*", end = "")
    for j in range(n - 1, 0, -1):
        if i - j >= 0:
            break
        else: print("*", end = "")
    print()
    i += 1

i -= 2

while i >= 0:
    for j in range(0, n):
        if i - j > 0:
            print(" ", end = "")
        else: print("*", end = "")
    for j in range(n - 1, 0, -1):
        if i - j >= 0:
            break
        else: print("*", end = "")
    print()
    i -= 1