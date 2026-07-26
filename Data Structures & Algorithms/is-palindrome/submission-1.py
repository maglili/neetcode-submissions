class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1 = 0
        p2 = len(s)-1
        chk_times = int(len(s) / 2)

        for _ in range(chk_times):
            while ((s[p1].isalpha() == False) and (s[p1].isdigit() == False)):
                p1+=1
            while ((s[p2].isalpha() == False) and (s[p2].isdigit() == False)):
                p2-=1
            char1 = s[p1].lower()
            char2 = s[p2].lower()
            if (char1 != char2):
                return False
            p1+=1
            p2-=1
        return True
            
