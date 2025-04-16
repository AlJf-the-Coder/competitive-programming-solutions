class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ind_dict = {}
        for i, num in enumerate(nums):
            ind_dict[num] = i

        for i, num in enumerate(nums):
            j = ind_dict.get(target - num, -1)
            if j >= 0 and j != i:
                return [i, j]
            
        
