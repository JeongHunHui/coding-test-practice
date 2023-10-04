class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start, c_tank, total_tank = 0, 0, 0
        for i in range(len(gas)):
            if c_tank < 0:
                start = i
                c_tank = 0
            amount = gas[i] - cost[i]
            c_tank += amount
            total_tank += amount
        return start if total_tank >= 0 else -1