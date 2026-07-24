class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            cur_num = nums[i]
            target = 0 - cur_num
            l = i + 1
            r = len(nums) - 1
            while ( l < r):
                l_num = nums[l]
                r_num = nums[r]
                if (l_num + r_num < target):
                    l = l + 1
                elif (l_num + r_num == target):
                    ans.append([cur_num, l_num, r_num])
                    l = l + 1
                    r = r - 1
                else: # (l_num + r_num > target)
                    r = r - 1
        unique_tuples =  set(tuple(sub) for sub in ans)
        return [list(t) for t in unique_tuples]
#[-4,-1,-1,0,1,2]