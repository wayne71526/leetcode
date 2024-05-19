# solution 1
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        comb = []

        def backtrack(start):
            if len(comb) == k:           # 總共有 k 層，因要 k 個數字
                ans.append(comb[:])      # 將 comb 新增到 ans
                return
            for num in range(start, n+1):
                comb.append(num)         # 對此層的 comb 新增數字
                backtrack(num+1)         # 進入下一層
                comb.pop()               # 將 comb 剛加入的數字刪除，方便找出此層下一個可能的組合
                
        backtrack(1)
        return ans

        
# solution 2
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtrack(start, comb):
            for num in range(start, n+1):
                new_comb = comb + [num]     # 對此層的 comb 新增數字得到 new_comb
                backtrack(num+1, new_comb)  # 進入下一層

            if len(comb) == k:              # 總共有 k 層，因要 k 個數字
                ans.append(comb)            # 將 comb 新增到 ans
                return
            
                
        backtrack(1, [])
        return ans

