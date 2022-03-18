# https://www.acmicpc.net/problem/14254

import sys, collections
input = sys.stdin.readline

password = input().strip()
K = int(input())
L = len(password)

if K == L: 
    print(0)
else:
    ans = 0
    if K*2 <= L:
        start = password[:K]
        end = password[L-K:]
        for i in range(K):
            if start[i] == end[i]:
                continue
            else:
                ans += 1
    else:
        diff = L-K
        for k in range(diff):
            chars = collections.defaultdict()
            len = 0
            for i in range(k, L, diff):
                if password[i] in chars:
                    chars[password[i]] += 1
                else:
                    chars[password[i]] = 1
                len += 1
            maxCnt = 0
            for count in chars.values():
                maxCnt = max(maxCnt, count)
            ans += (len-maxCnt)
    print(ans)