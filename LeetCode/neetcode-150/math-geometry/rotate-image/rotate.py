class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1
        while l < r:
            matrix[l], matrix[r] = matrix[r], matrix[l]
            l += 1
            r -= 1
        for i in range(len(matrix)):
                for j in range(i + 1, len(matrix)):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
                for j in range(i + 1, len(matrix)):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(len(matrix)):
            matrix[i].reverse()

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        new_matrix = [list(reversed([matrix[j][i] for j in range(len(matrix))])) for i in range(len(matrix))]
        for i in range(len(matrix)):
            matrix[i] = new_matrix[i]
