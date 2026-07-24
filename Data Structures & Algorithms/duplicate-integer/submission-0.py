class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        table = {}
        dup_frag = False
        for i in nums:
            if i not in table:
                table[i] = None
            else:
                dup_frag = True
        return dup_frag


