# ms solution

# 1. 算出 n!
# 2. 觀察 prod 可以被 10 整除幾次
class Solution:
    def trailingZeroes(self, n: int) -> int:
        l = list(range(1, n+1))

        prod = math.prod(l)
        count = 0
        while prod % 10 == 0:
            count += 1
            prod = prod // 10
        return count
        

# leetcode solution:

# 想法：藉由知道 n! 的質因數 5 有幾個來求得 n! 有幾個 0 
# 作法：
#      1. 算出 1 到 n 為 5^1 的倍數有幾個
#      2. 算出 1 到 n 為 5^2 的倍數有幾個
#      3. 以此類推....直到 n < 5^k，最後全部相加即為答案
class Solution:
    def trailingZeroes(self, n: int) -> int:
        i = 1
        count = 0

        while n // pow(5, i):
            count += n // pow(5, i)
            i += 1

        return count
        
