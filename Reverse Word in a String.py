class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()[::-1]      # 將 string s 以空格分開並將輸出的 list 倒序
        string = ' '.join(s)     # 將 list s 中的元素合併並且元素之間多加一個空格

        return string