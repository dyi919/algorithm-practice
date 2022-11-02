# https://leetcode.com/problems/where-will-the-ball-fall/

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ans = []
        M, N = len(grid), len(grid[0])

        def fall(x, y):
            if x == M:
                return y
            if grid[x][y] == 1:
                if y+1 < N and grid[x][y+1] == 1:
                    return fall(x+1, y+1)
                return -1
            else:
                if y-1 >= 0 and grid[x][y-1] == -1:
                    return fall(x+1, y-1)
                return -1

        for i in range(N):
            ans.append(fall(0, i))

        return ans