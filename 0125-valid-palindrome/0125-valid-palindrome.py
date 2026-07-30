class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = re.sub(r'[^a-zA-Z0-9]','',s)
        cleaned_string = cleaned_string.lower()
        i,j= 0, len(cleaned_string)-1
        while i < j:
            if cleaned_string[i] != cleaned_string[j]:
                return False
            else:
                i +=1
                j-=1
        return True
