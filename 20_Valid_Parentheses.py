# solution
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            '(':')',
            '[':']',
            '{':'}'
        }

        m = []

        for x in s:
            if x in dic:
                m.append(x)
            elif len(m) and dic[m[-1]] == x:  # m 不為空且 m 的最後一個括號與 x 為成對
                del m[-1]
            else:
                return False

        return not m