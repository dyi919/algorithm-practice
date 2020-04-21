# prints the average mark for 5 students

total = 0

for i in range(5):
    mark = int(input())
    if mark < 40:
        mark = 40
    total += mark

print(int(total/5))
