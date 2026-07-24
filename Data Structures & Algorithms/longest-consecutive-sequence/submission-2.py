class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 1. put all num in tbl
        num_tbl = set()
        for n in nums:
            num_tbl.add(n)
        
        # 2. scan all nums
        res = 0
        for n in nums:
            # impossible to be the start of the sequence
            if n - 1 in num_tbl:
                continue
            
            cnt = 0
            cur_num = n
            while cur_num in num_tbl:
                cur_num+=1
                cnt +=1
            if cnt > res:
                res = cnt
        return res
