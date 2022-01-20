from sys import stdin

_ = input()
cards = [int(i) for i in stdin.readline().split()]

cardsDict = {}

for num in cards:
    if num in cardsDict:
        cardsDict[num] += 1
    else:
        cardsDict[num] = 1

_ = input()
nums = [int(i) for i in stdin.readline().split()]

print(' '.join(str(cardsDict[i]) if i in cardsDict else '0' for i in nums))
