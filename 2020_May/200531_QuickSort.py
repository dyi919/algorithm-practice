def partition(arr, lo, hi):
    i = lo - 1
    pivot = arr[hi]

    for j in range(lo, hi):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
    return i + 1

def quickSort(arr, lo, hi):
    if lo < hi:
        pi = partition(arr, lo, hi)
        quickSort(arr, lo, pi - 1)
        quickSort(arr, pi + 1, hi)

arr = [1, 10, 5, 76, 32]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
print(arr)