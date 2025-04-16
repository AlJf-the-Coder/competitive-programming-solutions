class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        parity = nums[0] % 2
        for i in range(1, len(nums)):
            cur_parity = nums[i] % 2
            if parity == cur_parity:
                return False
            parity = cur_parity
        return True
