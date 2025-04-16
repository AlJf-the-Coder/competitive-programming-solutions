class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        min_reachable = n - 1
        for i in range(n - 2, -1, -1):
            if i + nums[i] >= min_reachable:
                min_reachable = i
        return min_reachable == 0

class Solution1:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[n - 1] = True
        for i in range(n - 2, -1, -1):
            dp[i] = any(dp[i + 1: i + nums[i] + 1])
        return dp[0]

class Solution2:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        marked = [False] * n
        def dfs(i):
            if i < 0 or marked[i]:
                return False
            if i == 0:
                return True
            marked[i] = True
            for j in range(i):
                if nums[j] >= i - j and dfs(j):
                    return True
            return False
        return dfs(n - 1)
