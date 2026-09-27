class Solution:
    def longestValidParentheses(self, s: str) -> int:
        #we initialise our stack as 
        stack = [-1] #as for now the current valid length starts from index 0
        maxLen = 0

        for i in range(len(s)):
            #the -1 exists to calculate the length of stack from the beginning element, but if the beginning element itself is invalid ie. ")". then we pop the -1 and append the latest nxt index
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()

                if not stack:
                    stack.append(i)
                else:
                    currentLen = i - stack[-1]
                    maxLen = max(currentLen, maxLen)
        return maxLen     
         