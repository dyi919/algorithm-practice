# repeat each character in the string r times

t = int(input())

for _ in range(t):
    r, s = input().split()
    r = int(r)

    for char in s:
        for i in range(r):
            print(char, end = "")
    print("")
