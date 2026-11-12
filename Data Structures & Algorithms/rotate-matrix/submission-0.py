class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix[0]) - 1

        while l < r:
            for i in range(r - l):    # range(l, r - 1) could have also worked. 
                top, bottom = l, r  #As it is an n x n matrix (basically a square matrix), therefore top and bottom will be equal to left and right pointers. 
                # save the top left(like a temporary variable)
                topLeft = matrix[top][l + i]
                # move bottom left into top left(doing this such that the counter-clockwise method stores only one temporary variable for the top left, instead of having three or four temporary variables)
                matrix[top][l + i] = matrix[bottom - i][l]

                #Move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                #Move top right to bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                #Move top left into top right
                matrix[top + i][r] = topLeft
            r -= 1
            l += 1   # No need for incrementing/decrementing top and bottom because top and bottom are, respectively, equivalent to left and right, as we have defined above. 