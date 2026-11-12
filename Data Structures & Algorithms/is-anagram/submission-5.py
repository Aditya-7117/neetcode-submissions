class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if Counter(s) == Counter(t) and set(s) == set(t):
            return True
        else: return False