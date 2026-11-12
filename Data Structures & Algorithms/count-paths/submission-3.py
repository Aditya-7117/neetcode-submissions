class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # As we know, the bottom row and rightmost column is all ones 
        row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j] # Right + bottom 
            row = newRow
        return row[0]
