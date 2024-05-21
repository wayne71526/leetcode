class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):      # 當 gas 總和比 cost 總和小，表示無法巡迴；相反，則可以巡迴
            return -1

        # 尋找起始 index
        start_index = 0
        current_gas = 0
        for i in range(len(gas)):
            current_gas += gas[i] - cost[i]   
            if current_gas < 0:               # 小於 0 表示此起始點無法巡迴，故下次檢查 i+1(起始點+1 到 i 不可能為解，因起始點+1 到 i 的總和小於 0)
                start_index = i + 1
                current_gas = 0

        return start_index

