class Solution:
    def isPalindrome(self, s: str) -> bool:
        list1 = []
        # left to right
        for char in s:
            if (char.isalpha() or char.isnumeric()):
                list1.append(char.lower())
        
        list2 = []
        # right to left
        for char in s[::-1]:
            if (char.isalpha() or char.isnumeric()): 
                list2.append(char.lower())

        return str(list1) == str(list2)