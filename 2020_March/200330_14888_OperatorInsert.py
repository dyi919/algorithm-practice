# put n-1 operators in between n numbers

def bfs(idx, add, sub, mul, div, result):
    global mx, mn

    if idx == n:
        mx = max(mx, result)
        mn = min(mn, result)
    
    if add < op[0]: bfs(idx + 1, add + 1, sub, mul, div, result + num[idx])
    if sub < op[1]: bfs(idx + 1, add, sub + 1, mul, div, result - num[idx])
    if mul < op[2]: bfs(idx + 1, add, sub, mul + 1, div, result * num[idx])
    if div < op[3]: bfs(idx + 1, add, sub, mul, div + 1, int(result / num[idx]))

mx = -1000000000
mn = 1000000000
n = int(input())
num = [int(x) for x in input().split()]
op = [int(x) for x in input().split()]

bfs(1, 0, 0, 0, 0, num[0])

print(mx)
print(mn)