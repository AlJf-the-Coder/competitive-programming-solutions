class Solution:
    def rob(self, nums: List[int]) -> int:
        one, two = 0, 0
        for num in nums:
            one, two = two, max(two, one + num)
        return two

class Solution1:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        res = [nums[0], max(nums[0], nums[1])]
        for i in range(2, n):
            res.append(max(res[i - 2] + nums[i], res[i - 1]))
        return res[n - 1]
