class Solution:
    def isPalindrome(self, x: int) -> bool:
        digits = []
        if x < 0:
            return False
        while x > 0:
            appendNumber = x % 10 # gives last digit of the number
            digits.append(appendNumber)
            x = x // 10 #removes last digit for the iteration
        return digits == digits[::-1]
        
        