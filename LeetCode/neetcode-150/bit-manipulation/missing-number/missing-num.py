class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        res ^= len(nums)
        for i in range(len(nums)):
            res ^= i
            res ^= nums[i]
        return res

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res += i - nums[i]
        return res

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        seen = [False] * (len(nums) + 1)
        for num in nums:
            seen[num] = True
        return seen.index(False)
