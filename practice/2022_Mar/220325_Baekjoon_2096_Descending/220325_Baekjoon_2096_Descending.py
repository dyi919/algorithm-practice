from sys import stdin, maxsize

N = int(input())
nums = [[int(x), int(x)] for x in stdin.readline().split()]

for _ in range(1, N):
    next = [[int(x), int(x)] for x in stdin.readline().split()]
    next[0][0] = max(nums[0][0], nums[1][0]) + next[0][0]
    next[0][1] = min(nums[0][1], nums[1][1]) + next[0][1]
    next[1][0] = max(nums[0][0], nums[1][0], nums[2][0]) + next[1][0]
    next[1][1] = min(nums[0][1], nums[1][1], nums[2][1]) + next[1][1]
    next[2][0] = max(nums[1][0], nums[2][0]) + next[2][0]
    next[2][1] = min(nums[1][1], nums[2][1]) + next[2][1]
    nums = next

print(max([x[0] for x in nums]), min(x[1] for x in nums))