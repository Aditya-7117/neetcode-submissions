class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1 # Bottom-up approach , only two spots of array required. That is why. 

        for i in range(n - 1):
            tmp = one #Temporary variable 
            one = one + two
            two = tmp 
        return one
