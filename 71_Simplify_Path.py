# solution
class Solution:
    def simplifyPath(self, path: str) -> str:
        name = []
        path = path.split('/')

        for s in path:
            if name and s == '..':            # 若 name 不是空的(空的表示目前為根目錄)且遇到'..'，則檔案位置要返回前一個
                del name[-1]
            elif s not in ['.', '', '..']:    # 若 s 不是 ['.', '', '..'] 當中的元素，則加進 name 中
                name.append(s)


        return '/' + '/'.join(name)