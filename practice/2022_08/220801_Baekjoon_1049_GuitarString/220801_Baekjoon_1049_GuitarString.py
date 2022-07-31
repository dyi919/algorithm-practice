# https://www.acmicpc.net/problem/1049

from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
package_price, unit_price = [0] * M, [0] * M
for i in range(M):
    package_price[i], unit_price[i] = map(int, input().split())

package_price.sort()
unit_price.sort()

min_price = 0

if N >= 6:
    if package_price[0] <= unit_price[0] * 6:
        min_price += package_price[0] * (N // 6)
        N %= 6
    else:
        min_price += unit_price[0] * N
        N = 0

if N > 0:
    if package_price[0] <= unit_price[0] * N:
        min_price += package_price[0]
    else:   
        min_price += unit_price[0] * N

print(min_price)
