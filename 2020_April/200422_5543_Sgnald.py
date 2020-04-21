# prints the cheapest set menu

burger = 0
drink = 0

for _ in range(3):
    price = int(input())
    if burger == 0 or burger > price:
        burger = price

for _ in range(2):
    price = int(input())
    if drink == 0 or drink > price:
        drink = price

print(burger + drink - 50)