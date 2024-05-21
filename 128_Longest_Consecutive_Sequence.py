# leetcode solution
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0

        # 1. 尋找起始點
        # 2. 若為起始點，觀察連續元素序列的長度
        # 3. 對答案做更新
        # for 迴圈的長度為 n，且 while 的長度也為 n(不是每個元素都要做 while)，故時間為 O(2n)=O(n)
        for num in nums:
            if (num - 1) not in nums:  # 若 (num - 1) 不在 nums 中，表示 num 為起始點
                l = 1
                curr_num = num
                while curr_num + 1 in nums:
                    l += 1
                    curr_num += 1
                
                ans = max(ans, l)

        return ans