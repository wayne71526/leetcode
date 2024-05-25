class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [(amount+1)] * (amount+1)    # 裝各個 amount 最少的 coin 數
        dp[0] = 0                         # amount 0 的最少 coin 數 

        for i in range(1, amount+1):
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i], dp[i-c] + 1)  # 將 c 塊換成 1 個 coin c看和原來的 coin 數哪個比較少

        return dp[-1] if dp[-1] != amount + 1 else -1