class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        l = 0
        r = 0
        while r < len(s):
            if s[l:r+1] not in wordDict:
                r+=1
            else:
                l = r+1
                r = l
        return True if l==r else False