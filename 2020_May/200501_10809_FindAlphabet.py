# Find each alphabet's first occurrence
from string import ascii_lowercase

s = input()
arr = [-1] * 26

for i in ascii_lowercase:
    if i in s:
        arr[ord(i) - 97] = s.index(i)

for a in arr:
    print(a, end=" ")