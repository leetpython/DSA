from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                complement_idx = hashmap[complement]
                return [i, complement_idx]
            hashmap[nums[i]] = i
