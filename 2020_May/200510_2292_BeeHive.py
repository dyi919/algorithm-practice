n = int(input())
i = 1
layer = 1

while i < n:
    i += layer * 6
    layer += 1

print(layer)