def bubbleSort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [100, 200, 150, 23, 50]

bubbleSort(arr)

print("Sorted array is: ")
for i in range(len(arr)):
    print("%d" %arr[i])