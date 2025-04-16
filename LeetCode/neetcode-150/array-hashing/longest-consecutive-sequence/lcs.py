from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_count = 0
        for num in set_nums:
            if num - 1 not in set_nums:
                count = 1
                val = num
                while val + 1 in set_nums:
                    count += 1
                    val += 1
                max_count = max(max_count, count)

        return max_count

class Solution1:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = sorted(set(nums))
        max_count = 0
        count = 1
        for i in range(1, len(set_nums)):
            if set_nums[i] == (set_nums[i - 1] + 1):
                count += 1
            else:
                max_count = max(max_count, count)
                count = 1
        return max(max_count, count)


