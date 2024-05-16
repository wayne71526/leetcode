# my solution
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        whole_intervals = sorted(intervals + [newInterval])   # 將兩個 list 合併，接著用 56 題的作法即可
        ans = [whole_intervals[0]]

        for interval in whole_intervals:
            if ans[-1][1] >= interval[0]:
                ans[-1][1] = max(ans[-1][1], interval[1])
            else:
                ans.append(interval)

        return ans


# leetcode solution
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []

        for i in range(len(intervals)):
            start, end = intervals[i]

            if start > newInterval[1]:
                ans.append(newInterval)
                return ans + intervals[i:]
            elif end < newInterval[0]:
                ans.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], start), max(newInterval[1], end)]
        
        ans.append(newInterval)   # 用在 newInterval 與最後一個 interval 有重疊時，還有 intervals == [] 時
        return ans