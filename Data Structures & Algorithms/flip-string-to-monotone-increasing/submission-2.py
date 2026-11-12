
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        countOne = 0
        flipZero = 0

        for i in s:
            if i == "1":
                countOne += 1
            else:
                # Two choices: flip current 0 to 1, or previous 1s to 0
                flipZero = min(flipZero + 1, countOne)

        # Minimum flips needed for the entire string
        return flipZero
