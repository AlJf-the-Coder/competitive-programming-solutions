class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        width = len(matrix[0])
        l = 0
        r = width * len(matrix) - 1
        while l <= r:
            mid = (l + r) // 2
            i = mid // width
            j = mid % width
            cur = matrix[i][j]
            if cur == target:
                return True
            elif cur < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
