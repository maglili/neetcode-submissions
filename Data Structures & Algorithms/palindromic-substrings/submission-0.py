class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        # dp[i,j] means s[i:j] is pali or not
        dp = [[0] * n for _ in range(n)]

        cnt = 0
        # i 從最後一個字元往回走（控制起點）
        for i in range(n - 1, -1, -1):
            # j 從 i 開始往後走（控制終點）
            for j in range(i, n):
                # 條件 1：頭尾字元要一樣
                # 條件 2：中間只有 0~1 個字元 (j-i <= 2) 或 內圈也是回文
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    cnt+=1
        
        return cnt
