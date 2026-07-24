class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt_tbl = {}
        arr_cnt = [ 0 for i in range(k)] # small to big
        arr_num = [ None for i in range(k)] # small to big
        for num in nums:
            # update tbl
            cnt_tbl[num] = cnt_tbl.get(num, 0) + 1
            appear_cnt = cnt_tbl[num]

            # if num in arr_num, just update the arr
            skip_frag = False
            for i in range(len(arr_num)):
                if arr_num[i] == num:
                    arr_cnt[i] = cnt_tbl[num]
                    skip_frag = True

            if skip_frag == True:
                continue

            # chk top k arr, find smallest one
            min_idx = find_small_pos(arr_cnt)

            # swap the smallest one
            if cnt_tbl[num] > arr_cnt[min_idx]:
                arr_cnt[min_idx] = cnt_tbl[num]
                arr_num[min_idx] = num
            
        return arr_num

def find_small_pos(arr):
    small_idx = 0
    small_num = arr[0]
    for i in range(len(arr)):
        if i == 0:
            continue
        if arr[i] < small_num:
            small_num = arr[i]
            small_idx = i
    return small_idx