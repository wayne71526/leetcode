# solution
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n      # dp[i]：nums[:i] 最長 subarray 的長度
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:               # 若 nums[i] > nums[j]，表示 nums[i] 可以加進 nums[:j] 最長 subarray 中
                    dp[i] = max(dp[i], dp[j]+1)     # 看 nums[i] 加進去後的長度，有沒有變的比 dp[i] 大，有表示長度需做更換

        return max(dp)