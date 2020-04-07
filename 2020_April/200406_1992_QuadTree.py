# get quad tree result

def quad(arr):
    ans = ""
    n = len(arr[0])

    if n == 1:
        ans = arr[0][0]

    else:
        half = int(n/2)
        lt = [[arr[i][j] for j in range(0, half)] for i in range(0, half)]
        rt = [[arr[i][j] for j in range(half, n)] for i in range(0, half)] 
        lb = [[arr[i][j] for j in range(0, half)] for i in range(half, n)] 
        rb = [[arr[i][j] for j in range(half, n)] for i in range(half, n)]

        ans = "("
        ans += quad(lt)
        ans += quad(rt)
        ans += quad(lb)
        ans += quad(rb)
        ans += ")"

        if len(ans) == 6:
            cnt = 0
            for num in ans[1:5]:
                if num == ans[1]: cnt += 1
            if cnt == 4:
                ans = ans[1]
         
    return ans

n = int(input())

arr = []

for _ in range(n):
    arr.append(list(input()))

ans = quad(arr)
print(ans)