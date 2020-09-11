def getSubset(ls, n, target):
    if target < 0 or n < 1:
        return

    if target == ls[n - 1]:
        yield [ls[n - 1]]
        return

    for subset in getSubset(ls, n - 1, target):
        yield subset

    for subset in getSubset(ls, n - 1, target - ls[n - 1]):
        yield subset + [ls[n - 1]]


arr = [1, 2, 6, 3, 17, 82, 23, 234]
target = 1
ls = [num for num in arr if num <= target]

sub = list(getSubset(ls, len(ls), target))

if sub == []:
    print("No subset with sum %d exists." % target)
else:
    sub = min(sub, key=len)
    ans = [i for i in range(len(arr)) if arr[i] in sub]
    print(ans)
