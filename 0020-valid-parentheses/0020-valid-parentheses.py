class Solution:
    def isValid(self, s: str) -> bool:

        #using basic stack structure we are going to initialise a frew parameters as explicitly given
        stack = []
        closeToOpen = {')':'(', '}':'{', ']':'['}

        for c in s: 
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]: #if stack is not empty and the top element of stack is closed parantheses
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False #if stack is empty after all iteration return true and false if still some elements stayed pending
        