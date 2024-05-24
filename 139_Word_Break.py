# solution
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False for _ in range(n+1)] 
        dp[n] = True                      # 空字串視為分割成功

        for i in range(n, -1, -1):
            for word in wordDict:
                if i+len(word) > n: 
                    continue

                # s[i:(i+len(word))] == word 表示若 s[(i+len(word)):n] 可分割，則 s[i:n] 也可分割；相反，則不行
                if s[i:(i+len(word))] == word:  
                    dp[i] = dp[i+len(word)]
 
                # 若 s[i:n] 可分割，則不用再檢查 s[i:n] 是否可分割
                if dp[i]:
                    break

        return dp[0]  # dp[0] 表示 s 是否可分割