# quick sort

def partition(arr, lo, hi):
    p = arr[int((lo + hi) / 2)]
    i = lo - 1
    j = hi + 1

    while True:
        while True:
            i += 1
            if arr[i] >= p: break
        while True:
            j -= 1
            if arr[j] <= p: break
        
        if i >= j: return j
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

def quickSort(arr, lo, hi):
    if lo < hi:
        p = partition(arr, lo, hi)
        quickSort(arr, lo, p)
        quickSort(arr, p + 1, hi)

n = int(input())
line = [int(x) for x in input().split()]
quickSort(line, 0, n - 1)
print(line)