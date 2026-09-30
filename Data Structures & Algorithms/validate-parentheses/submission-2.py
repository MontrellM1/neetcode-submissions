class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        d = {"}":"{", ")":"(", "]":"["}

        for char in s:
            if char not in d:
                stack.append(char)
            else:
                if not stack:
                    return False
                popped = stack.pop()

                if popped != d[char]:
                    return False

        if stack:
            return False
        return True
        
        
        