class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seem = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in seem:
                seem.remove(s[l])
                l += 1
            seem.add(s[r])
            res = max(res, r - l + 1)
        return res