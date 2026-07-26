class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.res = ""
        self.res_len = 0
        cur = []
        
        def dfs(i):
            if self.is_pali(cur) and len(cur) > self.res_len:
                self.res = "".join(cur.copy())
                self.res_len = len(cur)

            if i >= len(s):
                return

            # choose i
            cur.append(s[i])
            dfs(i + 1)

            # not choose i
            cur.pop()
            dfs(i + 1)

        dfs(0)
        return self.res

    def is_pali(self, arr):
        l = 0
        r = len(arr) - 1

        while l < r:
            if arr[l] != arr[r]:
                return False
            l += 1
            r -= 1
        return True
