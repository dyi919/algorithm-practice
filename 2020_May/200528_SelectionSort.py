import sys
arr = [15, 25, 10, 66, 34]

for i in range(len(arr)):
    minIdx = i
    for j in range(i + 1, len(arr)):
        if arr[minIdx] > arr[j]:
            minIdx = j
    
    arr[i], arr[minIdx] = arr[minIdx], arr[i]

print("Sorted array:")
for i in range(len(arr)):
    print("%d" %arr[i])