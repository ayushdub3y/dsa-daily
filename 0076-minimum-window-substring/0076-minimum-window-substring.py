class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        start = 0
        count = len(t)
        min_len = float("inf")
        freqMap = {}

        for char in t:
            freqMap[char] = freqMap.get(char, 0) + 1 #making the freqMap with the charcters we need and their respective frequencies

        #now we write a loop that right pointer moves until the end of string and checks
        for r in range(len(s)):
            char = s[r]
            if freqMap.get(char, 0) > 0: #character already present in the freqMap so reduce count (required) by 1
                count -= 1
            freqMap[char] = freqMap.get(char, 0) - 1 #decrease the frequency regardless

            while count == 0: #once the required count reaches 0, the i pointer has to shrink the window
                windowSize =  r - l + 1
                if windowSize < min_len:
                    min_len = windowSize
                    start = l
                
                left_char = s[l]
                freqMap[left_char] = freqMap.get(left_char, 0) + 1

                if freqMap[left_char] > 0:
                    count += 1 #required character
                l+=1
        if min_len == float("inf"):
                return ""
            
        return s[start:start + min_len]


                
        
