# find the max num in the array and print its index

mx = 0
idx = 0
arr = []

for i in range(9):
    n = int(input())
    arr.append(n)
    if mx < n:
        mx = n
        idx = i + 1

print(mx)
print(idx)