class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        window, mapT = defaultdict(int), defaultdict(int)
        
        for c in t:
            mapT[c] += 1
        
        have, need = 0, len(mapT)
        l = 0
        res, resLen = [-1, -1], float("infinity")
        for r in range(len(s)):
            window[s[r]] += 1

            if s[r] in mapT and window[s[r]] == mapT[s[r]]:
                have += 1
            
            while have == need:
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1
                if s[l] in mapT and window[s[l]] < mapT[s[l]]:
                    have -= 1
                l += 1
        l, r = res     
        return s[l: r + 1] if resLen != float("infinity") else ""