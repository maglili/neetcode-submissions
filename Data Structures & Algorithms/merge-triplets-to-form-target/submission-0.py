class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        x, y, z = 0, 0, 0
        for a, b, c in triplets:
            x = max(x, a)
            y = max(y, b)
            z = max(z, c)

            if [x, y, z] == target:
                return True
        return False
