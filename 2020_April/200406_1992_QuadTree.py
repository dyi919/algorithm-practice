# get quad tree result

import operator, sys

ans = ""

def check(arr):
    cnt = 0
    for line in arr:
        for char in line:
            if char == '1': cnt += 1

    if cnt == len(arr) * len(arr) or cnt == 0:
        return True
    else: 
        return False

def quad(arr):
    ans = "("
    n = len(arr[0])

    if n == 2: 
        ans += arr[0][0]
        ans += arr[0][1]
        ans += arr[1][0]
        ans += arr[1][1]

    else:
        half = int(n/2)
        lt, rt, lb, rb = ([[] * half for _ in range(half)] for _ in range(4))

        for i in range(n):
            if i < half:
                lt[i] = [x for x in arr[i][0 : half]]
                rt[i] = [x for x in arr[i][half : n]]

            else:
                lb[i - half] = [x for x in arr[i][0 : half]]
                rb[i - half] = [x for x in arr[i][half : n]]

        res = lt[0][0] if check(lt) else quad(lt)
        ans += res
        res = rt[0][0] if check(rt) else quad(rt)
        ans += res
        res = lb[0][0] if check(lb) else quad(lb)
        ans += res
        res = rb[0][0] if check(rb) else quad(rb)
        ans += res
        
    ans += ")"
    return ans

n = int(input())

arr = [[] * n for _ in range(n)]
line = []
result = ""

for i in range(n):
    arr[i] = [x for x in sys.stdin.readline().rstrip()]

ans = quad(arr)
print(ans)