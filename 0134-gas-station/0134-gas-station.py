class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total = 0
        tank = 0
        start = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total+= diff
            tank += diff

            if tank < 0:
                start = i+1
                tank = 0
        if total < 0:
            return -1
        return start

        