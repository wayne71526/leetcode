# solution
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        s = [nums[0]] * n
        s[0] = nums[0]                 # 若在 index 0 結束，最多可偷 nums[0]
        s[1] = max(nums[0], nums[1])   # 若在 index 1 結束，最多可偷 max(nums[0], nums[1])

        for i in range(2, n):
            s[i] = max(s[i-2]+nums[i], s[i-1])  # 若在 index i 結束，最多可偷 max(index i-2 結束時最多可偷到的錢 + nums[i], index i-1 結束時最多可偷到的錢)
            									#                               (若用 i-1 可能有 adjacent 的情形發生，故用 i-2)
        return s[-1]
