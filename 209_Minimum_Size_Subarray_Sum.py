# leetcode solution
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:  # 當 nums 總和小於目標值表示沒有解
            return 0
        
        # subarray 從第一個數開始
        # 1. 當總和 >= target，更新答案
        # 2. 將 subarray 最左邊的數字刪除，直到總和 < target 時停止，過程中若總和 >= target 同樣要更新答案
        # 3. 拓展 subarray 最右邊的數字直到總和 >= target，緊接著回到第一步驟

        left, s, ans = 0, 0, len(nums)

        for right, val in enumerate(nums):
            s += val
            while s >= target:
                ans = min(ans, right-left+1)
                s -= nums[left]
                left += 1

        return ans