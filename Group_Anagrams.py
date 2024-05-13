# my solution
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        # 1. 觀察 strs 的元素是由哪些字母組成(以 list 表示)，並且得到的 list 中的元素順序依照字母的先後順序排列
        # 2. 若此 list 在 dic 當中沒有，在字典新增新的類別；若有，則將 strs[i] 新增到此類別中
        for i in range(len(strs)):
            s = str(sorted([j for j in strs[i]]))
            if s not in dic:
                dic[s] = [strs[i]]
            else:
                dic[s].append(strs[i])

        return dic.values()


# leetcode solution
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for i in range(len(strs)):
            s = ''.join(sorted(strs[i]))  # sorted(strs[i]) 的結果為 list 形式
            dic[s].append(strs[i])

        return dic.values()
