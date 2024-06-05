# solution
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = ['+', '-', '*', '/']
        nums = []

        for i in tokens:
            if i not in operations:
                nums.append(int(i))
            else: 
                if i == '+':
                    result = nums[-2] + nums[-1]
                    del nums[-2:]
                    nums.append(result)
                elif i == '-':
                    result = nums[-2] - nums[-1]
                    del nums[-2:]
                    nums.append(result)
                elif i == '*':
                    result = nums[-2] * nums[-1]
                    del nums[-2:]
                    nums.append(result)
                elif i == '/':
                    result = nums[-2] / nums[-1]
                    del nums[-2:]
                    nums.append(int(result))

        return nums[-1]