class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # get median idx (upper bound)
        total = len(nums1) + len(nums2)
        med_idx = total // 2

        res, prev_res = 0, 0
        idx1,idx2 = 0, 0
        for _ in range(med_idx + 1):
            prev_res = res
            # both arr have num
            if idx1 < len(nums1) and idx2 < len(nums2):
                if nums1[idx1] <= nums2[idx2]:
                    res = nums1[idx1]
                    idx1 += 1
                else:
                    res = nums2[idx2]
                    idx2 += 1
            elif idx1 < len(nums1):
                res = nums1[idx1]
                idx1 += 1
            elif idx2 < len(nums2):
                res = nums2[idx2]
                idx2 += 1
            else:
                assert False
        if total % 2 == 0:
            return (res + prev_res) / 2
        return res
