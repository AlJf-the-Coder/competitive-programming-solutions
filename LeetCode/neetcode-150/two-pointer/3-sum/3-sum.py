class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        i = 0
        while i < n - 2:
            if nums[i] > 0:
                break
            target = -nums[i]
            j = i + 1
            k = n - 1
            while j < k:
                p_sum = nums[j] + nums[k]
                if p_sum == target:
                    res.append([nums[i], nums[j], nums[k]])
                    cur_k = nums[k]
                    cur_j = nums[j]
                    while j < k and nums[k] == cur_k:
                        k -= 1
                    while j < k and nums[j] == cur_j:
                        j += 1
                elif p_sum < target:
                    j += 1
                else:
                    k -= 1
            cur_i = nums[i]
            while i < n - 2 and nums[i] == cur_i:
                i += 1

        return res       

class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        seen = {}
        for j in range(1, n - 1):
            target = -nums[j]
            seen_j = seen.setdefault(nums[j], set())
            i = 0
            k = n - 1
            while i < j and k > j:
                while i < j and nums[i] in seen_j:
                    i += 1
                if i >= j:
                    break
                p_sum = nums[i] + nums[k]
                if p_sum == target:
                    res.append([nums[i], nums[j], nums[k]])
                    seen_j.add(nums[i])
                elif p_sum < target:
                    i += 1
                else:
                    k -= 1

        return res       

