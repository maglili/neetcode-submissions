class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = []
        for c in s:
            if c.isdigit() or c.isalpha():
                new_s.append(c.lower())
        s = "".join(new_s)
        
        l, r = 0, len(s) - 1
        while l < r:
            while not (s[l].isdigit() or s[l].isalpha()):
                l += 1
            while not (s[r].isdigit() or s[r].isalpha()):
                r -= 1
            if l > r:
                return
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True