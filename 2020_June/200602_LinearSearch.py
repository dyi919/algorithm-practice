def linearSearch(arr, n, x):
    for i in range(0, n):
        if arr[i] == x:
            return i
    
    return -1

arr = [1, 5, 10, 23, 34]
x = 23
n = len(arr)
result = linearSearch(arr, n, x)

if result == -1:
    print("Element not in array")
else:
    print("Element is at index %s" % result)