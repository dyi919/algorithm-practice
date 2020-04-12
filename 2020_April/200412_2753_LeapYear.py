# determine whether leap year or not

def isLeapYear(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return 1
            return 0
        return 1
    return 0

y = int(input())
print(isLeapYear(y))