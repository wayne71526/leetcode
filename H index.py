# 一個人在其所有學術文章中有 N 篇論文分別被引用了至少 N 次，h 指數就是 N 的最大值

# my solution
class Solution:
    def hIndex(self, citations: List[int]) -> int:
    	# 將每一篇論文引用次數由大到小排列
        citations = sorted(citations, reverse=True)
        final_h = temp_h = 0
        for i in range(len(citations)):
            temp_h = min(citations[i], i+1) # 計算可能的 h 值
            if final_h < temp_h:
                final_h = temp_h
            else:
                break

        return final_h



# leetcode solution
class Solution:
    def hIndex(self, citations: List[int]) -> int:
    	# 將每一篇論文引用次數由小到大排列
        citations.sort()
        h = len(citations) # h 的最大可能值
        for i in citations:
            if i < h:      # 根據定義 h 為 N 篇論文分別被引用了至少 N 次 N 的最大值，則不符合定義表示此 h 不是正確答案，將其減 1 檢查下一個可能的 h 值
                h -= 1
            else:
            	break

        return h
