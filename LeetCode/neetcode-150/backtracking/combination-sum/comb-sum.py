class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        res = []
        def help(arr, arr_sum, i):
            if arr_sum == target:
                res.append(arr)
            for j in range(i, n):
                if arr_sum + candidates[j] > target:
                    return
                help(arr + [candidates[j]], arr_sum + candidates[j], j)
        help([], 0, 0)
        return res

class Solution1:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        def help(arr, arr_sum, i):
            if arr_sum > target:
                return
            if i == n:
                if arr_sum == target:
                    res.append(arr)
                return
            help(arr + [candidates[i]], arr_sum + candidates[i], i)
            help(arr, arr_sum, i + 1)
        help([], 0, 0)
        return res
