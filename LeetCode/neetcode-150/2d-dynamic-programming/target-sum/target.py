class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n_sum = sum(nums)
        if target > n_sum or target < -n_sum:
            return 0
        dp = defaultdict(int)
        dp[0] = 1
        for num in nums:
            new_dp = defaultdict(int)
            for s in dp:
                if s - num >= -n_sum:
                    new_dp[s - num] += dp[s]
                if s + num <= n_sum:
                    new_dp[s + num] += dp[s]
            dp = new_dp

        return dp[target]

class Solution1:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n_sum = sum(nums)
        if target > n_sum or target < -n_sum:
            return 0
        dp = [0]*(2 * n_sum + 1)
        dp[-nums[0]] += 1
        dp[nums[0]] += 1
        prev_dp = dp.copy()
        for i in range(1, len(nums)):
            num = nums[i]
            prev_dp, dp = dp, prev_dp
            for s in range(-n_sum, n_sum + 1):
                dp[s] = 0
                if s - num >= -n_sum:
                    dp[s] += prev_dp[s - num]
                if s + num <= n_sum:
                    dp[s] += prev_dp[s + num]

        return dp[target]

class Solution2:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n_sum = sum(nums)
        if target > n_sum or target < -n_sum:
            return 0
        dp = [[0]*(len(nums)) for i in range(-n_sum, n_sum + 1)]
        dp[-nums[0]][0] += 1
        dp[nums[0]][0] += 1
        for i in range(1, len(nums)):
            num = nums[i]
            for s in range(-n_sum, n_sum + 1):
                if s - num >= -n_sum:
                    dp[s][i] += dp[s - num][i - 1]
                if s + num <= n_sum:
                    dp[s][i] += dp[s + num][i - 1]
        return dp[target][len(nums) - 1]
