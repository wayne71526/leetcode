class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        s = board[0][0]
        m = len(board)
        n = len(board[0])

        def backtrack(r, c, k):  # k 為 word 的位置
            if k == len(word):
                return True
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[k]:
                return False

            temp = board[r][c]          # 為了避免重複走，將 board[r][c] 先用變數存起來，再將空字串指定給 board[r][c]
            board[r][c] = ''

            # 若 4 個方向中有 return True，表示已找到 word
            if backtrack(r+1, c, k+1) or backtrack(r-1, c, k+1) or backtrack(r, c-1, k+1) or backtrack(r, c+1, k+1):
                return True

            board[r][c] = temp          # 若沒有找到 word 則要換成下一個起始值尋找，故要將原來的 board 的數值放回去
            return False

        for r in range(m):
            for c in range(n):
                if backtrack(r, c, 0):
                    return True
        
        return False