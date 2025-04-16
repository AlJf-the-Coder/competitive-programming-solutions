class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -float('inf')
        neg_sub = 1
        pos_sub = 1
        for num in nums:
            pos_sub, neg_sub = max(num, neg_sub * num, pos_sub * num), min(num, neg_sub * num, pos_sub * num)
            res = max(res, pos_sub)
        return res

class Solution1:
    def maxProduct(self, nums: List[int]) -> int:
        res = -float('inf')
        neg_sub = float('inf')
        pos_sub = -float('inf')
        for num in nums:
            if num > 0:
                neg_sub = neg_sub * num
                pos_sub = max(num, pos_sub * num)
            elif num < 0:
                pos_sub, neg_sub = neg_sub * num, min(num, pos_sub * num)
            else:
                neg_sub = 0
                pos_sub = 0
            res = max(res, pos_sub)
            if neg_sub != float('inf'):
                res = max(res, neg_sub)
        return res
