# Tpwer of Hanoi

srcArr = []
destArr = []

def Hanoi(num, src, dest, thru):
    if num == 1: 
        srcArr.append(src)
        destArr.append(dest)
    else: 
        Hanoi(num - 1, src, thru, dest)
        srcArr.append(src)
        destArr.append(dest)
        Hanoi(num - 1, thru, dest, src)

n = int(input())

Hanoi(n, "1", "3", "2")

print(len(srcArr))

for i in range(len(srcArr)):
    print(srcArr[i], destArr[i])