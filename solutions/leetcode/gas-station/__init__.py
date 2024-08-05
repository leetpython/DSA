from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)

        # Determine if we have a solution
        total_surplus = sum(gas[i] - cost[i] for i in range(N))
        if total_surplus < 0:
            return -1

        # Now, we know a solution exists.
        # Let's find a station to start from.
        tank = 0
        start = 0
        for i in range(N):
            tank += gas[i] - cost[i]

            # If the tank becomes negative here, we can't start from
            # wherever we last chose. So, it's better to start from the
            # next station.
            if tank < 0:
                start = i + 1
                tank = 0

        return start
