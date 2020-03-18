# A program that takes two integer inputs a and b, and prints a + b

caseNum = int(input())
sumArr = []

for i in range(caseNum):
    temp = input().split()
    a = int(temp[0])
    b = int(temp[1])
    
    sumArr.append(a + b)

for i in range(caseNum):
    print(sumArr[i])
