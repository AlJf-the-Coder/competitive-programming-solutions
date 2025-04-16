class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def help(i):
            if i == n:
                res.append(list(nums.copy()))
                return
            for j in range(i, n):
                nums[j], nums[i] = nums[i], nums[j]
                help(i + 1)
                nums[j], nums[i] = nums[i], nums[j]
        help(0)
        return res

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        n = len(nums)
        seen = [False for i in range(n)]
        def help(i):
            if i == n:
                res.append(list(perm))
                return
            for j in range(n):
                if not seen[j]:
                    seen[j] = True
                    perm.append(nums[j])
                    help(i + 1)
                    perm.pop()
                    seen[j] = False
        help(0)
        return res

class Solution1:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        n = len(nums)
        def help(arr, i):
            if i == n:
                res.append(list(perm))
                return
            for j, num in enumerate(arr):
                perm.append(num)
                help(arr[:j] + arr[j + 1:], i + 1)
                perm.pop()
        help(nums, 0)
        return res
