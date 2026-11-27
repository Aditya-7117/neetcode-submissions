class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        # We are going to do it in true DP way, that is, bottom-up. 
        for i in range(len(s) - 1, - 1, -1):
            for w in wordDict:
                if (i + len(w) <= len(s) and (s[i: i + len(w)] == w)):
                    #The above first condition checks if the word is not out of the string, and the second condition checks if current string matches word 
                    dp[i] = dp[i + len(w)] # This means the word from the main string is found similar to the word from the word dictionary. Then at the end of the word, there will also be similarity. of dp
                if dp[i] == True:
                    break
        return dp[0]