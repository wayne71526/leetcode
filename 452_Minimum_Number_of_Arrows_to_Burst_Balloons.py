# my solution
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points)
        ans = [points[0]]

        for point in points:
            if ans[-1][1] < point[0]:
                ans.append(point)
            else:
                # 尋找兩 interval 間重疊的範圍，箭射在這範圍，這些有重疊部分的 interval 的氣球都會被射爆
                ans[-1][0] = max(ans[-1][0], point[0])  
                ans[-1][1] = min(ans[-1][1], point[1])

        return len(ans)


# leetcode solution
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points)
        arrows = 1
        end = points[0][1]

        for point in points:
            if end < point[0]:             # 兩 interval 不重疊，故 箭數 + 1 才能將氣球打完
                arrows += 1
                end = point[1]       
            else:
                end = min(end, point[1])   # 得到兩 interval 重疊的上界，用以觀察下一個 interval 是否與這些 interval 重疊

        return arrows