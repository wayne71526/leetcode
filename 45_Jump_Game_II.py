# my solution
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        pos = 0
        count = 0
        next_pos = 0

        if n == 1:
            return 0

        while pos + nums[pos] < n-1:
            count += 1                    
            final_maxi = 0           
            for i in range(nums[pos]+1):
                if i == 0:
                    continue
                maxi = pos + i + nums[pos+i]
                if maxi > final_maxi:
                    final_maxi = maxi
                    next_pos = pos + i
            if final_maxi >= n-1:
                return count + 1
            pos = next_pos

        if pos + nums[pos] >= n-1:
            return 1



# leetcode solution
class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = end = farthest = 0
        for i in range(len(nums)-1):
            farthest = max(farthest, nums[i]+i) # 找這次 jump 可以跳到的最遠位置
            if farthest >= len(nums)-1: 
                ans += 1                        # 當最遠的位置已超出範圍時直接輸出答案
                break
            if i == end:                        # 若 i 為上一次 jump 可以跳到的最遠位置，實施 jump(故 ans +1)，並且將 end 用這次 jump 可以跳到的最遠位置取代
                ans += 1                        
                end = farthest
        
        return ans