class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        char_tbl1 = {}
        char_tbl2 = {}
        for i in range(len(s)):
            char_tbl1[s[i]] = char_tbl1.get(s[i], 0) + 1
            char_tbl2[t[i]] = char_tbl2.get(t[i], 0) + 1

        return char_tbl1 == char_tbl2
        