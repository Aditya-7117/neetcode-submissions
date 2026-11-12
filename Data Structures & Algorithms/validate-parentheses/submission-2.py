class Solution:
    def isValid(self, s: str) -> bool:
        closingSet = {"]" : "[", "}" : "{", ")" : "("}
        stack = []

        for i in s:
            if i in closingSet:
                if stack and stack[-1] == closingSet[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else  False
                    
                    