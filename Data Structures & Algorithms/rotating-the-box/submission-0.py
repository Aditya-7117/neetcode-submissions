class Solution:
    def rotateTheBox(self, grid: List[List[str]]) -> List[List[str]]:
        rows, cols = len(grid), len(grid[0])
        #Update positions. 
        for r in range(rows):
            i = cols - 1
            for c in reversed(range(cols)):
                if grid[r][c] == "#":
                    grid[r][c], grid[r][i] = grid[r][i],  grid[r][c]
                    i -= 1
                elif grid[r][c] == "*":
                    i = c - 1

        res = []

        for c in range(cols):
            col = []
            for r in reversed(range(rows)):
                col.append(grid[r][c])
            res.append(col)
        return res


