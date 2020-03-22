# Prints the number of Han numbers between 1 and N (inclusive, N <= 1000)
# Han number is defined as a certain integer whose digits make an arithmetical progression

def isHan(x):
    hundreds = int(x / 100)
    tens = int((x - 100 * hundreds) / 10)
    ones = x % 10
     
    if hundreds - tens == tens - ones: return True
    else: return False
            
n = int(input())

if n < 100: print(n)
else:
    total = 99
    for i in range(100, n + 1):
        if isHan(i): total += 1
    print(total)