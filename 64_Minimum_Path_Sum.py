# solution
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0] * len(grid[i]) for i in range(len(grid))]
        dp[0][0] = grid[0][0]

        for i in range(0, len(grid)):
            for j in range(len(grid[i])):
                if i == 0 and j == 0:
                    continue

                if i == 0:                                 
                    dp[i][j] = dp[i][j-1] + grid[i][j]  
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]     
                else:
                    dp[i][j] = min(dp[i][j-1] + grid[i][j], dp[i-1][j] + grid[i][j])
        
        return dp[-1][-1]

