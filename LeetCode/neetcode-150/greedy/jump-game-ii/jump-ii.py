class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[n - 1] = 0
        min_reachable = n - 1
        for i in range(n - 2, -1, -1):
            if i + nums[i] >= min_reachable:
                dp[i] = 1 + min(dp[min_reachable: i + nums[i] + 1])
                min_reachable = i
        return dp[0]

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[n - 1] = 0
        reachable = [n - 1]
        for i in range(n - 2, -1, -1):
            for r in reversed(reachable):
                if i + nums[i] >= r:
                    dp[i] = min(dp[i], dp[r])
                else:
                    break
            dp[i] += 1
            if dp[i] != float('inf'):
                reachable.append(i)
            
        return dp[0]



