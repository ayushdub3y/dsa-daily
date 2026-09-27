class Solution:
    def isValid(self, s):
        stack = []
        closeToOpen = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }

        for bracket in s:
            if bracket in closeToOpen: #it is a closed bracket
                if not stack:
                    return False
                top = stack.pop()
                if closeToOpen[bracket] != top:
                    return False
            else:
                stack.append(bracket) #open bracket, add in the stack
        if not stack:
            return True
        else:
            return False