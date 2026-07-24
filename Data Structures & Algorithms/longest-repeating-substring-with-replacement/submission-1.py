class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0 # remember the max count  to speed up
        for r in range(len(s)):
            # upd count 
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]])

            # chk window valid
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1  #pop l
                l += 1

            # upd res
            res = max(res, r - l + 1)

        return res