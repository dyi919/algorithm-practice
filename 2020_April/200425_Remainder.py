# prints how many different remainders exist for dividing each of the 10 numbers by 42

arr = []

for _ in range(10):
    isExist = False
    n = int(input())
    rem = n % 42
    for num in arr:
        if num == rem:
            isExist = True
    if not isExist:
        arr.append(rem)
    

print(len(arr))