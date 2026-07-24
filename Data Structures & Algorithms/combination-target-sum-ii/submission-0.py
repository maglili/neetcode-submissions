class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # sort candidates
        candidates.sort()

        res = []
        cur = []

        def dps(i, cur_sum):
            if cur_sum == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or cur_sum > target:
                return

            # choose this idx
            cur.append(candidates[i])
            dps(i+1, cur_sum + candidates[i])

            # not choose (keep pop the same num)
            cur.pop()
            while i < (len(candidates) - 1) and candidates[i+1] == candidates[i]:
                i = i + 1
            dps(i+1, cur_sum)
        
        dps(0, 0)
        return res
