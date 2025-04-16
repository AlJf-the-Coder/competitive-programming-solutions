class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        res = 0
        tank = 0
        for i in range(len(cost)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                res = i + 1
        return res
    
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        l = r = 0
        n = len(cost)
        tank = gas[l] - cost[l]
        while True:
            if tank >= 0 :
                r = (r + 1) % n
                if l == r:
                    break
                tank += gas[r] - cost[r]
            else:
                l = (l - 1) % n
                tank += gas[l] - cost[l]     
        return l
