class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M = len(word1)
        N = len(word2)
        memo = {} # (i, j): val

        def dfs(i, j):
            if i == M:  # word1 run out of character
                return N - j  # word1 add char
            if j == N:  # word2 run out of character
                return M - i  # word1 delete char
            if (i, j) in memo:
                return memo[(i, j)]

            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)

            res = min(dfs(i + 1, j), dfs(i, j + 1))  # insert, delete
            res = min(res, dfs(i + 1, j + 1))  # replace
            memo[(i, j)] = res + 1

            return res + 1

        return dfs(0, 0)
