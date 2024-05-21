# 因可以循環，則有兩種情形：
# 1. 不用循環即可找到 subarray 的總和最大值，如：[1,3,-1,-2]
# 2. 需循環才能找到 subarray 的總和最大值，如：[5,-3,-2,5]
# 2 的情形中 subarray 的總和最大值可看成 array 的總和 - 不循環的 subarray 的總和最小值

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if max(nums) <= 0:
            return max(nums)

        totalsum, maxsum, minsum = 0, -math.inf, math.inf
        currmaxsum, currminsum = 0, 0

        for num in nums:
            totalsum += num
            currmaxsum = max(num, currmaxsum+num)
            currminsum = min(num, currminsum+num)

            maxsum = max(maxsum, currmaxsum)
            minsum = min(minsum, currminsum)


        return max(maxsum, totalsum-minsum)
        