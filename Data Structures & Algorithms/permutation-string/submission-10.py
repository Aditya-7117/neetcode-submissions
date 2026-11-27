class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1map = defaultdict(int)
        windowmap = defaultdict(int)
        l = 0
        
        for c in s1:
            s1map[c] += 1
        
        for r in range(len(s2)):
            windowmap[s2[r]] += 1

            if r - l + 1 > len(s1):
                windowmap[s2[l]] -= 1 
                if windowmap[s2[l]] == 0:
                    del windowmap[s2[l]]
                l += 1         
            
            if  r - l + 1 == len(s1) and windowmap == s1map:
                return True
            
        return False