# stack sum, pop when input is 0

k = int(input())
stack = []

for _ in range(k):
    n = int(input())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)

print(sum(stack))