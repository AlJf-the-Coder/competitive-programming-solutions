class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        q = deque()
        cnt = 1
        visited = [False] * (amount + 1)
        for c in coins:
            if c <= amount:
                q.append(c)
                visited[c] = True
        while q:
            for i in range(len(q)):
                amt = q.popleft()
                if amt == amount:
                    return cnt
                for c in coins:
                    if c + amt <= amount and not visited[c + amt]:
                        q.append(c + amt)
                        visited[c + amt] = True
            cnt += 1

        return 0 if amount == 0 else -1

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        n = len(coins)
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin < 0:
                    break
                dp[i] = min(dp[i], 1 + dp[i - coin])

        return dp[amount] if dp[amount] != float('inf') else -1

class Solution1:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        @cache
        def backtrack(amt):
            if amt == 0:
                return 0
            res = float('inf')
            for i in range(n):
                if amt - coins[i] < 0:
                    break
                res = min(res, 1 + backtrack(amt - coins[i]))
            return res
        res = backtrack(amount)
        return  res if res != float('inf') else -1

class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        @cache
        def backtrack(i, amt):
            if amt == 0:
                return 0
            if i == n or amt < 0:
                return float('inf')
            res = min(float('inf'), backtrack(i + 1, amt))
            res = min(res, 1 + backtrack(i, amt - coins[i]))
            return res
        res = backtrack(0, amount)
        return  res if res != float('inf') else -1
