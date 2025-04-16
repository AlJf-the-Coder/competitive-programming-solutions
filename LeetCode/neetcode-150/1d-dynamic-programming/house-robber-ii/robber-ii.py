class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        one, two_1 = 0, 0
        for i in range(n - 1):
            one, two_1 = two_1, max(two_1, one + nums[i])
        one, two_2 = 0, 0
        for i in range(1, n):
            one, two_2 = two_2, max(two_2, one + nums[i])
        return max(nums[0], two_1, two_2)

class Solution1:
    def rob(self, nums: List[int]) -> int:
        max_profit = 0
        n = len(nums)
        for i in range(n):
            idx = (i - n + 2) % n
            one, two = 0, 0
            while idx != i:
                one, two = two, max(two, one + nums[idx])
                idx = (idx + 1) % n
            max_profit = max(max_profit, max(two, one + nums[idx]))
        return max_profit
