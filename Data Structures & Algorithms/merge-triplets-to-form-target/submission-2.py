class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        seen = set()
        for tri in triplets:
            if tri[0] > target[0] or tri[1] > target[1] or tri[2] > target[2]:
                continue
            for i in range(len(target)):
                if tri[i] == target[i]:
                    seen.add(i)

        return len(seen) == len(target)
