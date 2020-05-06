# find the most frequent alphabet in a word

word = input()
arr = [0] * 26

for char in word:
    arr[ord(char.upper()) - 65] += 1

m = max(arr)
maxArr = [i for i, j in enumerate(arr) if j == m]

if len(maxArr) > 1:
    print("?")
else:
    print(chr(maxArr[0] + 65))