class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        res = 0
        max_freq = 0 # remember the max freq to speed up
        for r in range(len(s)):
            # upd freq
            freq[s[r]] = freq.get(s[r], 0) + 1
            max_freq = max(max_freq, freq[s[r]])

            # chk window valid
            while r - l + 1 - max_freq > k:
                freq[s[r]] = freq[s[r]] - 1
                l += 1

            # upd res
            res = max(res, r - l + 1)

        return res