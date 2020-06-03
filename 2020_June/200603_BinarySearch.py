def binarySearch(arr, l, r, x):
    if r >= 1:
        mid = l + (r - l) // 2

        if arr[mid] == x:
            return mid
        
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)
        
        else:
            return binarySearch(arr, mid + 1, r, x)
    
    else:
        return -1

arr = [1, 6, 21, 25, 46]
x = 46

result = binarySearch(arr, 0, len(arr) - 1, x)

if result == -1:
    print("Element not in array")
else:
    print("Element is at index %d" % result)