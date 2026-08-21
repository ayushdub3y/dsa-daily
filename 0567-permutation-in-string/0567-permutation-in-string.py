class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #firstly the  basic algorithm is that we get our i and j pointers and for every iteration we have to maintain a window of size len(s1). not smaller, not bigger.
        #for every iteration i and j get incremented by 1 each and the frequency map of i, j window is compared with s1 and the answer can EASILY be returned
        n = len(s1)
        window = {}
        window_s1 = {}

        if len(s2) < n:
            return False

        for char in s1:
            window_s1[char] = window_s1.get(char, 0) + 1

        if len(s2) < n:
            return False
        
        i = 0

        for j in range(len(s2)):
            window[s2[j]] = window.get(s2[j], 0) + 1

            if j-i+1 > n:
                window[s2[i]] -=1

                if window[s2[i]] == 0:
                    del window[s2[i]]

                i+=1
                
            if j-i+1 == n and window == window_s1:
                return True
        return False

        