class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else: # This is important. For handling the * symbol 
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMax < 0: #Coxnfirmed that there is no chance of recovery. 
                return False
            if leftMin < 0: # s = (*)(
                leftMin = 0
        return leftMin == 0 