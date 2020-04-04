# G(n) = G(n - 1) + G(n - 2) + G(n - 3)

base = [0, 1, 1]

def G(n, arr: list):
    if n == 0:
        return 0
    if n < 3:
        return 1
    
    if n == 3: 
        return sum(arr)
    
    return G(n - 1, [arr[1], arr[2], sum(arr)])

for i in range(10):
    print("G", i, "=", G(i, base))
