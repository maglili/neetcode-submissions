class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx1 in range(len(numbers)):
            for idx2 in range(idx1, len(numbers)):
                if numbers[idx1] + numbers[idx2] == target:
                    return [idx1+1, idx2+1]