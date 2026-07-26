class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        res = -1
        LEN = len(gas)
        for i in range(LEN):
            fuel = gas[i]  # init fuel
            fee = cost[i]
            sucess = True

            for j in range(1, LEN + 1):
                fuel -= fee
                if fuel < 0:
                    sucess = False
                    break
                # add fuel
                idx = (i + j) % LEN
                fuel += gas[idx]
                fee = cost[idx]
            res = i if sucess else -1
        return res
