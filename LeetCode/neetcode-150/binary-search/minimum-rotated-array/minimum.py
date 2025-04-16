class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            if nums[l] <= nums[r]:
                return nums[l]
            mid = (l + r) // 2
            if nums[l] > nums[mid]:
                l += 1
                r = mid
            elif nums[mid] > nums[r]:
                l = mid + 1
