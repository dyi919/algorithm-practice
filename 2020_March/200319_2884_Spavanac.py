# Set the alarm 45 minutes early

temp = input().split()
h = int(temp[0])
m = int(temp[1])

if m < 45:
    m = 60 - (45 - m)
    
    if h == 0: h = 23
    else: h -= 1

else: m -= 45

print(h, m)