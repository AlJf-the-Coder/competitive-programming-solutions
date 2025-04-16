class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
            else:
                l = 0
                r = len(dp)
                idx = -1
                while l < r:
                    mid = (l + r) // 2
                    if dp[mid] >= nums[i]:
                        idx = mid
                        r = mid
                    else:
                        l = mid + 1
                dp[idx] = nums[i]
        return len(dp)

class Solution1:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], dp[j])
            dp[i] += 1
        return max(dp)

class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def backtrack(i):
            if i == len(nums):
                return 0
            res = 0
            for j in range(i + 1, len(nums)):    
                if nums[j] > nums[i]:
                    res =  max(res, backtrack(j))
            return 1 + res

        res = 0
        for i in range(len(nums)):
            res = max(res, backtrack(i))
        return res
