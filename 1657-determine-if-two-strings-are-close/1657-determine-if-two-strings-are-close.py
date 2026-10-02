class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        m = len(word1)
        n = len(word2)
        arr1, arr2 = [0] * 26, [0]*26

        if m != n:
            return False #if lengths are not equal then theres no point comparing

        for char in word1:
            idx = ord(char) - ord('a')
            arr1[idx] += 1
        
        for char in word2:
            idx = ord(char) - ord('a')
            arr2[idx] += 1

        for i in range(26):
            if arr1[i] != 0 and arr2[i] != 0:
                continue
            if arr2[i] == 0 and arr1[i] == 0:
                continue
            return False                # if any characters in word1 are not in word2 or vice versa
            
        return sorted(arr1) == sorted(arr2)
        

