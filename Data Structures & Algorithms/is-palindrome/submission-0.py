class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        newstring = ''
        for c in s:
            if c.isalnum():
                newstring += c.lower()

        return newstring == newstring[::-1]