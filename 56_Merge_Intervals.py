# my solution
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        l = len(intervals)
        start, end = intervals[0][0], intervals[0][1]
        ans = []

        for i in range(l-1):
            if end < intervals[i+1][0]:            # 看此 interval 是否與下一個 interval 有所重疊
                ans.append([start, end])           # 不重疊直接將此 interval 加入到 ans 中
                start = intervals[i+1][0]
                end = intervals[i+1][1]
            else:
                end = max(end, intervals[i+1][1])  # 重疊時將這兩個 interval 合併
           
        ans.append([start, end])                   # i==l-2 時，不管 l-2 的 interval 和 l-1 的 interval 有無重疊，合併後或 l-1 的 interval 需新增至 ans
        return ans                                 # l==1 時，也需此指令將僅有的 interval 新增至 ans


# leetcode solution
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        ans = [intervals[0]]

        for interval in intervals:
            if ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
           
        return ans