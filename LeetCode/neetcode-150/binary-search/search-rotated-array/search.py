class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        n = len(nums)
        r = n - 1
        
        while l <= r:
            if nums[l] <= nums[r]:
                m =  l
                break
            mid = (l + r) // 2
            if nums[l] > nums[mid]:
                l += 1
                r = mid
            elif nums[mid] > nums[r]:
                l = mid + 1
        
        if m > 0 and nums[0] <= target <= nums[m - 1]:
            l = 0
            r = m - 1
        elif nums[m] <= target <= nums[n - 1]:
            l = m
            r = n - 1
        else:
            return -1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
        
        return -1
        


