# https://www.acmicpc.net/problem/1107

from sys import stdin
from itertools import product
from bisect import bisect_left
input = stdin.readline

N = int(input())
M = int(input())

len_digits = len(str(N))
without_num_buttons = abs(100-N)
if N == 100:
    print(0)
elif M == 0:
    print(min(without_num_buttons, len_digits))
elif M == 10:
    print(without_num_buttons)
else:
    smaller_closest, larger_closest = 0, 0 
    broken_buttons = list(map(int, input().split()))
    buttons = [str(x) for x in range(10) if x not in broken_buttons]
    permutation = list(map(int, list(map(''.join, list(map(list, (product(buttons, repeat=len_digits))))))))
    idx = bisect_left(permutation, N)
    
    if idx == 0:
        larger_closest = permutation[idx]
        if larger_closest >= 10:
            smaller_closest = permutation[idx-1] // 10
        else:
            smaller_closest = permutation[idx]
    else:
        smaller_closest = permutation[idx-1]
        if idx == len(permutation):
            if '0' not in buttons:
                larger_closest = int(buttons[0] * (len_digits+1))
            elif len(buttons) == 1:
                larger_closest = 0
            else:
                larger_closest = int(buttons[1] + buttons[0] * len_digits)
        else:
            larger_closest = permutation[idx]
            
    closest = smaller_closest if N - smaller_closest <= larger_closest - N else larger_closest
    print(min(without_num_buttons, len(str(closest))+abs(N-closest)))