class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        row_set = set()
        col_set = set()

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    row_set.add(r)
                    col_set.add(c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if r in row_set or c in col_set:
                    matrix[r][c] = 0
        

