# my solution 
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for index1 in range(len(numbers)-1):
            another = target - numbers[index1]            # 尋找第二個 index 
            if another in numbers[(index1+1):]:           # 若 another 有在 numbers[(index1+1):] 中就找出 index2
                index2 = numbers[(index1+1):].index(another) + index1 + 1
                return [index1+1, index2+1]




# leetcode solution
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end   = len(numbers) - 1
        while start < end:
            if numbers[start] + numbers[end] == target:
                return [start+1, end+1]
            elif numbers[start] + numbers[end] > target:
                end -= 1
            else:
                start += 1
        
        return [-1, -1]