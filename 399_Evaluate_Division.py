class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dics = defaultdict(dict)

        for (i, j), val in zip(equations, values):
            dics[i][i] = 1
            dics[j][j] = 1
            dics[i][j] = val
            dics[j][i] = 1 / val

        for i in dics:
            # 將 dics[i] 中的 key 做組合，形成新的 equation
            for j in dics[i]:
                for k in dics[i]: 
                    dics[j][k] = dics[j][i] * dics[i][k] if j != k else 1

        return [dics[i].get(j, -1) for i, j in queries]