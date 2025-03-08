class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        rect = 0
        stack = []
        for i, h in enumerate(heights):
            if stack:
                if h == stack[-1][1]:
                    continue
                j = i
                while stack and h < stack[-1][1]:
                    j, hi = stack.pop()
                    rect = max(rect, hi * (i - j))
                i = j
            stack.append((i, h))

        while stack:
            i, h = stack.pop()
            rect = max(rect, h * (n - i))
        return rect        

class Solution1:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        rect = 0
        for i, h in enumerate(heights):
            width = 1
            for j in range(i - 1, -1, -1):
                if heights[j] >= h:
                    width += 1
                else:
                    break
            for j in range(i + 1, n):
                if heights[j] >= h:
                    width += 1
                else:
                    break
            rect = max(rect, h * width)
        return rect
            
        
