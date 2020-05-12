x = int(input())

i = 1
sum = 0

while sum < x:
    sum += i
    i += 1

sum += 1

if i % 2 == 0:
    numerator = sum - x
    denominator = i - numerator
else:
    denominator = sum - x
    numerator = i - denominator

print("%d/%d" % (numerator, denominator))