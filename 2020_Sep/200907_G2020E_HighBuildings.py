def HighBuildings():
    T = int(input())
    for t in range(T):
        N, A, B, C = [int(x) for x in input().split()]
        possible = True
        arr = [1 for _ in range(N)]

        if A + B - C > N:
            possible = False
        elif C > A or C > B:
            possible = False
        elif N > 1 and A == 1 and B == 1:
            possible = False
        else:
            if A > C or B > C:
                mid = len(arr)//2
                arr[mid] = N
                i = 1
                cnt = 1
                lo, hi = mid, mid
                while cnt < C:
                    if arr[mid-i] != N:
                        arr[mid-i] = N
                        lo = mid - i
                    else:
                        arr[mid+i] = N
                        hi = mid + i
                        i += 1
                    cnt += 1
                i = 0

                if A < B:
                    arr = arr[lo-(A-C):] + arr[:lo-(A-C)]
                    lo = A - C
                    hi = lo + C - 1
                    while C + i < B:
                        arr[len(arr) - 1 - i] = N - 1
                        i += 1
                elif A > B:
                    A, B = B, A
                    arr = arr[lo-(A-C):] + arr[:lo-(A-C)]
                    lo = A - C
                    hi = lo + C - 1
                    while C + i < B:
                        arr[len(arr) - 1 - i] = N - 1
                        i += 1
                    arr = arr[::-1]
                else:
                    while C + i < A:
                        arr[i], arr[len(arr) - 1 - i] = N - 1, N - 1
                        i += 1
            else:
                cnt = 0
                i = 0
                while cnt < C:
                    if arr[i] != N:
                        arr[i] = N
                    else:
                        arr[len(arr)-1-i] = N
                        i += 1
                    cnt += 1

        if possible:
            print("Case #%d:" % (t+1), *arr, sep=' ')
        else:
            print("Case #%d: IMPOSSIBLE" % (t+1))


HighBuildings()
