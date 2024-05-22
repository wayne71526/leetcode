# my solution
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1


        while left < right:
            mid = (left + right)//2

            # 往高處走，才能找到 peak。 若 if 和 elif 皆不符合，表示 mid 是 peak。
            if nums[mid] < nums[mid + 1]:    
                left = mid + 1
            elif nums[mid] < nums[mid - 1]:  
                right = mid - 1
            else:
                return mid

        return left