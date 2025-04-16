class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        max_so_far = 0
        while i != j:
            if height[i] < height[j]:
                max_so_far = max(max_so_far, (j - i) * height[i])
                i += 1
            else:
                max_so_far = max(max_so_far, (j - i) * height[j])
                j -= 1
        return max_so_far

        '''
        n = len(height)
        area = 0
        for i in range(n):
            for j in range(i + 1, n):
                dist = j - i
                h = min(height[i], height[j])
                c_area = h * dist
                if c_area > area:
                    area = c_area
        return area
        '''
