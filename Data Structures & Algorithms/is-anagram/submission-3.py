class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tbl1 = {}
        tbl2 = {}
        for char in s:
            tbl1[char] = tbl1.get(char, 0) + 1
        for char in t:
            tbl2[char] = tbl2.get(char, 0) + 1
        return tbl1 == tbl2