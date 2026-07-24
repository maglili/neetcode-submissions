class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uni_num = set(nums)

        max_con_cnt = 0
        for num in uni_num:
            # find start of sequence
            if (num - 1) in uni_num:
                continue
            
            # count consecutive times
            len_ = 1
            while (num + len_) in uni_num:
                len_+=1
            
            # update max_con_cnt
            max_con_cnt = max(max_con_cnt, len_)

        return max_con_cnt
                