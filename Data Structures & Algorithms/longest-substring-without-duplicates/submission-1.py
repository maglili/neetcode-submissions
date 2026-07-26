class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        cnt = 0
        max_cnt = 0
        for char in s:
            if char not in seen:
                seen[char] = True
                cnt += 1
            else:
                seen = {char:True}
                max_cnt = max(max_cnt, cnt)
                cnt = 1
        return max(max_cnt, cnt)