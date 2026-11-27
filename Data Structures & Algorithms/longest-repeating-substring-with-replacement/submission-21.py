class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        charMap = defaultdict(int)
        maxf= 0 

        for r in range(len(s)):
            charMap[s[r]] += 1

            maxf = max(maxf, charMap[s[r]])
            if (r - l + 1) - maxf > k:
                charMap[s[l]] -= 1
                l += 1
        return r - l + 1
