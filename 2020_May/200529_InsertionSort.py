def insertionSort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        
        arr[j + 1] = key

arr = [10, 5, 20, 23, 1]
insertionSort(arr)
print("Sorted array: ")
print(arr)