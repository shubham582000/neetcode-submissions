class Solution:
    def isPalindrome(self, s: str) -> bool:
        lo = 0
        high = len(s)-1
        while(lo<high):
            while lo<high and not s[lo].isalnum():
                lo+=1
            while lo<high and not s[high].isalnum():
                high-=1
            if s[lo].lower() != s[high].lower():
                return False
            lo+=1
            high-=1
        return True

        