# how many times each number appears in the digits of a * b * c

arr = [0] * 10
a = int(input())
b = int(input())
c = int(input())

num = a * b * c

while num > 0:
    i = num % 10
    arr[i] += 1
    num //= 10

for i in range(0, 10):
    print(arr[i])