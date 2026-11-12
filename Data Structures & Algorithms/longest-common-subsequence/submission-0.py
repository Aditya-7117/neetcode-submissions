class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int: 
        #Bottom-up approach 
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)] # 2D grid of length rows +1  and columns + 1
        #Starting at the bottom right of the grid 
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1] #Diagonal 

                else:
                    dp[i][j] = max(dp[i + 1][j],dp[i][j + 1])

        return dp[0][0]
        