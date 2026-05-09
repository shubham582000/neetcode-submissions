class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash = {}
        for strr in s:
            if strr not in hash:
                hash[strr] = 0
            hash[strr] += 1
        for ch in t:
            if ch not in hash:
                return False
            hash[ch] -= 1
            if hash[ch] < 0:
                return False
        return True

        