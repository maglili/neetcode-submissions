class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uni_num = set()
        for num in nums:
            uni_num.add(num)

        max_con_cnt = 0
        for num in uni_num:
            # find start of sequence
            if (num - 1) in uni_num:
                continue
            
            # count consecutive times
            cur_con_cnt = 0
            cur_num = num
            while (1):
                if cur_num in uni_num:
                    cur_con_cnt+=1
                    cur_num+=1
                else:
                    break
            
            # update max_con_cnt
            if (cur_con_cnt > max_con_cnt):
                max_con_cnt = cur_con_cnt
        return max_con_cnt
                