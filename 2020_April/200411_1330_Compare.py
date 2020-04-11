# compare two numbers

x, y = [int(x) for x in input().split()]

if x > y:
    print(">")
elif x < y:
    print("<")
elif x == y:
    print("==")