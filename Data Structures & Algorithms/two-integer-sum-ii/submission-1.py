class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = len(numbers) - 1
        l = 0

        # reduce r
        while (numbers[l] + numbers[r] > target):
            r = r - 1

        while (numbers[l] + numbers[r] != target):
            if (numbers[l] + numbers[r]) > target:
                r = r - 1
            else:
                l = l + 1

        return [l +1, r+1]