from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        sums = set([0])
        for i in range(len(nums) - 1, -1, -1):
            new = set()
            for t in sums:
                if t == total // 2 or t + nums[i] == total // 2:
                    return True
                if t + nums[i] < total // 2:
                    new.add(t + nums[i])
            sums.update(new)
        return False

class Solution2:
    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def backtrack(acc_sum, i):
            if i == len(nums):
                return acc_sum == total // 2
            return backtrack(acc_sum , i + 1) or \
                    backtrack(acc_sum + nums[i] , i + 1)
        total = sum(nums)
        if total % 2 == 1:
            return False
        return backtrack(0, 0)

