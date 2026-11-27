class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        charMap = defaultdict(int)
        windowMap = defaultdict(int)
        l = 0

        for s in s1:
            charMap[s] += 1

        for r in range(len(s2)):
            windowMap[s2[r]] += 1

            if r - l + 1 == len(s1):
                if charMap == windowMap:
                    return True
                windowMap[s2[l]] -= 1
                if windowMap[s2[l]] == 0:
                    del windowMap[s2[l]]
                l += 1
        return False
