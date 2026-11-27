class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)

        dp[0] = 0
        #For the other DPs [dp[1] .. dp[amount]]
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a -c])
                                    #Above 1 came because we are using a coin currently. 
        return dp[amount] if dp[amount] != amount + 1 else -1