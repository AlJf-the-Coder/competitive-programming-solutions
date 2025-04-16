class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #rows
        seen_boxes = [[0] * 3 for i in range(3)]
        seen_rows = [0] * 9
        seen_cols = [0] * 9
        div_inds = dict([(i, i//3) for i in range(9)])
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': 
                    continue
                int_cell = int(board[i][j]) - 1
                mask = 1 << int_cell
                if mask & seen_rows[i] or mask & seen_cols[j] or mask & seen_boxes[div_inds[i]][div_inds[j]]:
                    return False
                else:
                    seen_rows[i] |= mask
                    seen_cols[j] |= mask 
                    seen_boxes[div_inds[i]][div_inds[j]] |= mask
                        
        return True
            
class Solution1:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #rows
        seen_boxes = [[set() for j in range(3)] for i in range(3)]
        seen_rows = [set() for i in range(9)]
        seen_cols = [set() for j in range(9)]
        div_inds = dict([(i, i//3) for i in range(9)])
        for i in range(9):
            seen_row = seen_rows[i]
            for j in range(9):
                seen_col = seen_cols[j]
                seen_box = seen_boxes[div_inds[i]][div_inds[j]]
                if board[i][j] == '.': 
                    continue
                if board[i][j] in seen_row or board[i][j] in seen_col or board[i][j] in seen_box:
                    return False
                else:
                    seen_row.add(board[i][j])
                    seen_col.add(board[i][j])
                    seen_box.add(board[i][j])
                        
        return True
