class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = [[] for _ in range(9)]
        row, col = [], []
        for y in range(9):
            row = []
            for x in range(9):
                if board[y][x] != '.':
                    boxes[3*(y//3) + x//3].append(board[y][x])
                    row.append(board[y][x])
            if len(set(row)) != len(row): return False
            
        for x in range(9):
            col = []
            for y in range(9):
                if board[y][x] != '.':
                    col.append(board[y][x])
            if len(set(col)) != len(col): return False
        
        for v in boxes:
            if len(set(v)) != len(v):
                return False
        
        return True
                
                                        
                