class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        tbl = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
            "0":"+",
        }

        res = []
        cur = [] 
        
        def dfs(i):
            if i >= len(digits):
                print(cur)
                res.append("".join(cur))
                return
            
            choice = tbl[digits[i]]
            for char in choice:
                cur.append(char)
                dfs(i+1)
                cur.pop()

        if digits != "":
            dfs(0)
        return res
