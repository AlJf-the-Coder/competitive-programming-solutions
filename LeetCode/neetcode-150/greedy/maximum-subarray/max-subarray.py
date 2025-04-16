class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = 0
        for num in nums:
            if cur_sum <= 0:
                cur_sum = num
            else:
                cur_sum += num
            max_sum = max(max_sum, cur_sum)
        return max_sum

class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = nums[0]
        for i in range(n):
            cur_sum = 0
            for j in range(i, n):
                cur_sum += nums[j]
                max_sum = max(max_sum, cur_sum)
        return max_sum
