n = int(input())

count = 0

for _ in range(n):
    word = input()
    arr = [0] * 26
    prev = ""
    for char in word:
        if prev != char:
            arr[ord(char.upper()) - 65] += 1
        prev = char

    if max(arr) == 1:
        count += 1

print(count)