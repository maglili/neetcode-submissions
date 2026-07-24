class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_tbl1 = {}
        char_tbl2 = {}
        for char in s:
            char_tbl1[char] = char_tbl1.get(char, 0) + 1
        for char in t:
            char_tbl2[char] = char_tbl2.get(char, 0) + 1
        
        for key, val in char_tbl1.items():
            if char_tbl1[key] != char_tbl2.get(key, 0):
                return False
        
        for key, val in char_tbl2.items():
            if char_tbl2[key] != char_tbl1.get(key, 0):
                return False     

        return True
        