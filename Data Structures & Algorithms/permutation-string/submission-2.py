class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1map = defaultdict(int)
        
        l = 0
        
        for c in s1:
            s1map[c] += 1
        
        for r in range(len(s2) - len(s1) + 1):
            windowmap = defaultdict(int)
            window = s2[l: l + len(s1)]
            
            for w in window:
                windowmap[w] += 1
            
            if windowmap == s1map:
                return True
            l += 1
            
        return False