class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r = len(grid)
        c = len(grid[0])
        ans = 0

        def dfs(row, column):
            if (not (0 <= row and row < r)) or (not (0 <= column and column < c)) or (grid[row][column] == '0'):
                return

            grid[row][column] = '0' # 將 1 變成 0 表示已看過
            dfs(row-1, column)
            dfs(row, column-1)
            dfs(row+1, column)
            dfs(row, column+1)

        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(i, j)
            
        return ans