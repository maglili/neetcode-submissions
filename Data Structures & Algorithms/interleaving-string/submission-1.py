class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        N = len(s1)
        M = len(s2)

        if (N + M) != len(s3):
            return False

        # dp[m][n]
        # s1[:m] and s2[:n] can build s3[:m+n-1]
        dp = [[False] * (M + 1) for _ in range(N + 1)]
        dp[0][0] = True

        for i in range(N + 1):
            for j in range(M + 1):
                if i == 0 and j == 0:
                    continue

                k = i + j - 1

                if i > 0:
                    if s1[i - 1] == s3[k] and dp[i - 1][j]:
                        dp[i][j] = True

                if j > 0:
                    if s2[j - 1] == s3[k] and dp[i][j - 1]:
                        dp[i][j] = True

        return dp[N][M]
