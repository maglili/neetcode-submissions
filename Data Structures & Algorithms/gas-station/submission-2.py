class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total_fuel = 0
        start_idx = 0
        for i in range(len(gas)):
            total_fuel += (gas[i] - cost[i])

            if total_fuel < 0:
                start_idx = i + 1
                total_fuel = 0
        return start_idx