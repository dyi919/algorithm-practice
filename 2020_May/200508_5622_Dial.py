import math

s = input()
time = 0

for char in s:
    num = ord(char) - 64
    if num <= 15:
        time += math.ceil(num / 3) + 2
    elif num <= 19:
        time += 8
    elif num <= 22:
        time += 9
    else:
        time += 10

print(time)