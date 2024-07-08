class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        def dfs(r, c):
            board[r][c] = '#'
            for i, j in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if (0 <= i and i < m) and (0 <= j and j < n):
                    if board[i][j] == 'O':
                        dfs(i, j)

        # 與 boundary 的 O 相連的 O 換成 #(表示無法用 X 包圍)
        for i in range(m):
            if board[i][0] == 'O':
                dfs(i, 0)

            if board[i][n-1] == 'O':
                dfs(i, n-1)

        for j in range(n):
            if board[0][j] == 'O':
                dfs(0, j)

            if board[m-1][j] == 'O':
                dfs(m-1, j)

        # 將 # 換成 O，將 O 換成 X
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

                if board[i][j] == '#':
                    board[i][j] = 'O'

        return board