class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res += [subset + [num] for subset in res]
        return res

class Solution1:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def help(arr, i):
            if i == n:
                res.append(arr)
                return
            help(arr + [nums[i]], i + 1)
            help(arr, i + 1)
        help([], 0)
        return res
