class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        freq1 = {}
        freq2 = {}
        l = 0
         #Count characters in S1
        for c in s1:
            freq1[c] = freq1.get(c,0) + 1

        # for r in range(len(s2)):
        #     freq2[s2[r]] = freq2.get(s2[r], 0) + 1
        for r in range(len(s2) - len(s1) + 1):
            w = s2[l:l + len(s1)]

            if r == 0:
                for c in w:
                    freq2[c] = freq2.get(c,0) + 1
            
            else:
                freq2[w[-1]] = freq2.get(w[-1], 0) + 1
 
            if freq1 == freq2:
                return True
            
            else:
                freq2[w[0]] -= 1
             
            if freq2[w[0]] == 0:
                del freq2[w[0]]
            
            l += 1
        return False