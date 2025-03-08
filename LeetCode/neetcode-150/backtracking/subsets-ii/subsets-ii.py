class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        def help(arr, i):
            res.append(arr)
            for j in range(i, n):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                help(arr + [nums[j]],  j + 1)
        help([], 0)
        return res

class Solution1:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        def help(arr, i):
            if i == n:
                res.append(arr)
                return
            help(arr + [nums[i]],  i + 1)
            k = i + 1
            while k < n and nums[k] == nums[k - 1]:
                k += 1
            help(arr, k)
        help([], 0)
        return res

class Solution2:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        keys = sorted(counts)
        n = len(keys)
        def help(arr, i):
            if i == n:
                res.append(arr)
                return
            add = []
            for j in range(counts[keys[i]]):
                add.append(keys[i])
                help(arr + add,  i + 1)
            help(arr, i + 1)
        help([], 0)
        return res
