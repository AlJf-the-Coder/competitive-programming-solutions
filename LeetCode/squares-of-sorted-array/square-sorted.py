class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2

        merged = []
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] > nums[r]:
                merged.append(nums[l])
                l += 1
            else:
                merged.append(nums[r])
                r -= 1
                
        merged.reverse()
        return merged

class Solution1:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        neg = []
        pos = []

        for num in nums:
            if num < 0:
                neg.append(num ** 2)
            else:
                pos.append(num ** 2)
        neg.reverse()

        merged = []
        i = j = 0
        while i < len(neg) and j < len(pos):
            if neg[i] < pos[j]:
                merged.append(neg[i])
                i += 1
            else:
                merged.append(pos[j])
                j += 1

        if i < len(neg):
            merged.extend(neg[i:])
        if j < len(pos):
            merged.extend(pos[j:])
        
        return merged
