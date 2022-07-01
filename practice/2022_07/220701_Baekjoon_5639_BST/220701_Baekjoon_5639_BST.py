# https://www.acmicpc.net/problem/5639

from sys import stdin, setrecursionlimit
from collections import deque

setrecursionlimit(10**6)
input = stdin.readline
nums = []

while True:
    try:
        num = int(input())
        nums.append(num)
    except:
        break

def preorder_to_postorder(start, end):
    if start > end:
        return
    
    mid = end + 1

    for i in range(start+1, end+1):
        if nums[start] < nums[i]:
            mid = i
            break

    preorder_to_postorder(start+1, mid-1)
    preorder_to_postorder(mid, end)
    print(nums[start])
    
preorder_to_postorder(0, len(nums)-1)