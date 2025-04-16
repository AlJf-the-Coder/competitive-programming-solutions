class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        n = len(nums)
        for i in range(n):
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = nums[0]
        for i in range(n):
            if slow == slow2:
                return slow
            slow = nums[slow]
            slow2 = nums[slow2]
            
class Solution1:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        freqs = [0] * n
        for num in nums:
            freqs[num - 1] += 1
        for i in range(n):
            if freqs[i] > 1:
                return i + 1
