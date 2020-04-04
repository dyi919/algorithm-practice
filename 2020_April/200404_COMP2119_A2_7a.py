# Reverse an array using recursion

import sys

def reverse(arr):
    if len(arr) == 2:
        temp = arr[0]
        arr[0] = arr[1]
        arr[1] = temp
        return arr
    elif len(arr) == 3:
        temp = arr[0]
        arr[0] = arr[2]
        arr[2] = temp
        return arr
    
    front = []
    back = []
    result = []

    for i in range(0, int(len(arr)/2)): # 0~half
        front.append(arr[i])

    for i in range(int(len(arr)/2), len(arr)):
        back.append(arr[i])
    
    result = reverse(back)
    result.extend(reverse(front))
    return result

arr = [int(x) for x in sys.stdin.readline().split()]

print(reverse(arr))