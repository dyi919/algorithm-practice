# prints nth fibonacci num

def fibo(n, val, prev):
    if n == 0 or n == 1:
        return val + prev
    else:
        return fibo(n - 1, val + prev, val)

n = int(input())
print(fibo(n, 0, 1))