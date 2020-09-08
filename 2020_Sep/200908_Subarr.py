SUB = []


def getSubset(ls, n, target):
    subset = ([float('inf') for i in range(target + 1)] for i in range(n+1))


arr = [1, 2, 5, 5, 7, 2]
target = 10

ls = arr.copy()
ls.sort()

while len(ls) != 0 and ls[-1] > target:
    ls.pop(-1)

print(ls)

print("Ans:", list(getSubset(ls, target)))
