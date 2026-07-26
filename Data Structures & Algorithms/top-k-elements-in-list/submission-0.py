class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt_tbl = {}
        arr_cnt = [ None for i in range(k)] # small to big
        arr_num = [ None for i in range(k)] # small to big
        for num in nums:
            # update tbl
            cnt_tbl[num] = cnt_tbl.get(num, 0) + 1

            if cnt_tbl[num] in arr_num:
                continue
            
            # chk top k arr, find smallest one
            min_idx = find_small_pos(arr_cnt)

            if arr_cnt[min_idx] == None:
                arr_cnt[min_idx] = cnt_tbl[num]
                arr_num[min_idx] = num

            # swap the smallest one
            elif cnt_tbl[num] > arr_cnt[min_idx]:
                arr_cnt[min_idx] = cnt_tbl[num]
                arr_num[min_idx] = num
            
        return arr_num

def find_small_pos(arr):
    small_idx = 0
    small_num = arr[0]
    for i in range(len(arr)):
        if arr[i] == None:
            return i
        if i == 0:
            continue
        if arr[i] < small_num:
            small_num = arr[i]
            small_idx = i
    return small_idx