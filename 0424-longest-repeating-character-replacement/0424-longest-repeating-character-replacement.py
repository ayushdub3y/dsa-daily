class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #we define all the data structures and pointers we will need to solve this problem
        count = {}
        left = 0
        maxFreq = 0
        ans = 0

        for right in range(len(s)): 
            #right pointer has to look for possible windows until the end of the array
            char = s[right]
            count[char] = count.get(char, 0) + 1
            #this is to ensure everytime the right pointer reaches an element so the frequency is 0 (if not present already in count dict) else just get the current freq and update by 1
            maxFreq = max(maxFreq, count[char]) 
            #everytime we reach a new character and update its frequency, we can check if the char has reached the max freq in the count
            while (right-left + 1) - maxFreq > k:
                count[s[left]] -= 1
                left += 1
                #if the window shrinks the count of left element has to be decremented in order to update our freq map
            ans = max(ans, right-left+1)
        return ans