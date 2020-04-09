# quick sort and binary search

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

def binSearch(arr, lo, hi, n):
    mid = int((lo + hi) / 2)
    if arr[mid] == n:
        return 1
    elif arr[mid] > n:
        if mid <= lo: return 0
        return binSearch(arr, lo, mid - 1, n)
    elif arr[mid] < n :
        if mid >= hi: return 0
        return binSearch(arr, mid + 1, hi, n)

n = int(input())
line = [int(x) for x in input().split()]
quickSort(line, 0, n - 1)
m = int(input())
find = [int(x) for x in input().split()]
for num in find:
    print(binSearch(line, 0, n - 1, num))