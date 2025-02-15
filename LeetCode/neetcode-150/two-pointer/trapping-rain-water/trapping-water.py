from collections import deque
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = 0
        l = 0
        r = n - 1
        left_max = height[l]
        right_max = height[r]

        while l < r:
            if left_max <= right_max:
                water += left_max - height[l]
                l += 1
                left_max = max(left_max, height[l])
            else:
                water += right_max - height[r]
                r -= 1
                right_max = max(right_max, height[r])

        return water


from collections import deque
class Solution1:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = 0
        max_suffix = deque([0])
        for i in range(n - 1, 0, -1):
            max_suffix.appendleft(max(height[i], max_suffix[0]))
        max_prefix = [0]
        for i in range(n - 1):
            max_prefix.append(max(height[i], max_prefix[-1]))

        for i in range(n):
            min_height = min(max_prefix[i], max_suffix[i])
            if height[i] < min_height:
                water += min_height - height[i]

        return water

    
                

class Solution2:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = [0 for _ in range(n)]
        l = 0
        while l < n - 1:
            if height[l] == 0:
                l += 1
                continue
            cur_max = l + 1
            for r in range(l + 1, n):
                if height[r] >= height[l]:
                    cur_max = r
                    break
                if height[cur_max] < height[r]:
                    cur_max = r
                    
            min_height = min(height[l], height[cur_max])
            if min_height == 0:
                break #nothing to right
            for i in range(l + 1, cur_max):
                water[i] = max(water[i], min_height - height[i])
            l = cur_max
                
        return sum(water)


