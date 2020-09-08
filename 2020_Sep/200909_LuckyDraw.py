from time import sleep
from random import randrange

names = input().split()

for i in range(10):
    for j in range(5):
        print("두구", end='')
        sleep(0.05)
    print()

for i in range(3):
    print(".")
    sleep(1)

print("%s님 축하합니다~~" % names[randrange(len(names))])
