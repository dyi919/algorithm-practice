def longestAri():
    T = int(input())

    for t in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        prev = arr[1] - arr[0]
        cnt = 2
        maxCnt = 2

        for i in range(1, N - 1):
            diff = arr[i+1] - arr[i]
            if diff == prev:
                cnt += 1
                maxCnt = max(maxCnt, cnt)
            else:
                prev = diff
                cnt = 2

        print("Case #%d: %d" % (t + 1, maxCnt))


longestAri()
