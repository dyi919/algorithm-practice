# get minimum number of coins needed to become a value of k

coins = []
cnt = 0
mxIdx = 0

n, k = map(int, input().split())

for i in range(n): 
    coins.append(int(input()))
    if coins[i] > k and mxIdx == 0:
        mxIdx = i

if mxIdx == 0: mxIdx = len(coins)


for i in range(1, mxIdx + 1):
    if coins[mxIdx - i] <= k:
        cnt += int(k / coins[mxIdx - i])
        k = k % coins[mxIdx - i]

print(cnt)