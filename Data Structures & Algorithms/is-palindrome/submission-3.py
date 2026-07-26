class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while not (s[l].isdigit() or s[l].isalpha()):
                l += 1
            while not (s[r].isdigit() or s[r].isalpha()):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True