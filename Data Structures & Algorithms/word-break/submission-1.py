class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        # A[i] = s[i:] can be segmented into dict
        A = [False] * (n + 1)
        A[n] = True # base case.

        for i in range(n-1, -1, -1):
            for w in wordDict:
                # 1. i tp end have enough char
                # 2. s[i:i + len(w)] is match the w
                if i + len(w) <= n and s[i:i + len(w)] == w:
                    # update A[i] to True if before also True
                    if A[i+len(w)] == True:
                        A[i] = True
                        continue
        
        return A[0]