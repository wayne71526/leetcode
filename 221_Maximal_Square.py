# solution
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        l1, l2 = len(matrix), len(matrix[0])
        dp = [[0]*l2 for i in range(l1)]

        max_size = 0
        for i in range(l1):
            for j in range(l2):
                if matrix[i][j] =='1':
                    if i == 0 or j == 0:
                        dp[i][j] = int(matrix[i][j])
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

                max_size = max(max_size, dp[i][j])

        return max_size ** 2