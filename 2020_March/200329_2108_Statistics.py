# average median mode range

import sys

def printAverage(numArr, sum):
    print(round(sum / len(numArr)))

def printMedian(numArr):
    print(numArr[int(len(numArr) / 2)])

def printMode(numArr):
    if len(numArr) == 1: print(numArr[0])
    elif len(numArr) == 2: print(numArr[1])
    else:
        isSecond = False
        cnt = 1
        max = 1
        mode = numArr[0]

        for i in range(1, len(numArr)):
            if numArr[i] == numArr[i - 1]: 
                cnt += 1
                if max < cnt: 
                    max = cnt
                    mode = numArr[i]
                    isSecond = False
            else: cnt = 1
            if max == cnt and mode != numArr[i] and not isSecond:
                mode = numArr[i]
                isSecond = True

        print(mode)

def printRange(numArr):
    print(numArr[len(numArr) - 1] - numArr[0])

n = int(sys.stdin.readline())
num = []
sum = 0

for i in range(n): 
    num.append(int(sys.stdin.readline()))
    sum += num[i]

num.sort()
printAverage(num, sum)              # average
printMedian(num)               # median
printMode(num)                 # mode
printRange(num)                # range