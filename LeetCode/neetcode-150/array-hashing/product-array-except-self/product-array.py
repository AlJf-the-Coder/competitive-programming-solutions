from collections import deque
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = deque()
        products = []
        prod = 1
        n = 0
        for num in nums:
            n += 1
            prod *= num
            prefix.append(prod)
        prod = 1
        for num in reversed(nums):
            prod *= num
            suffix.appendleft(prod)
        products.append(suffix[1])
        for i in range(1, n - 1):
            products.append(prefix[i - 1] * suffix[i + 1])
        products.append(prefix[n - 2])
        return products
