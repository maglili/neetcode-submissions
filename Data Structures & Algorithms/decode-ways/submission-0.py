class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        n = len(s)
        A = [0] * (n + 1) # A[i] = 位置 i 可能的 decode 方式
        A[0] = 1 # 很反直覺?
        A[1] = 1 # 只有一種解法

        for i in range(2, n+1):
            if s[i-1] != "0":
                A[i] += A[i-1]

            digit = int(s[i-2:i])
            if 10<= digit <= 26:
                A[i] += A[i-2]

        return A[n]

