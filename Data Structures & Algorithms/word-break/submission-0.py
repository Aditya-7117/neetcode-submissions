class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        # We are going to do it in true DP way, that is, bottom-up. 
        for i in range(len(s) - 1, - 1, -1):
            for w in wordDict:
                if (i + len(w) <= len(s) and (s[i: i + len(w)] == w)):
                    dp[i] = dp[i + len(w)]
                if dp[i] == True:
                    break
        return dp[0]