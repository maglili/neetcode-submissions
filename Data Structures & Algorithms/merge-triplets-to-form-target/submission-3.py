class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        seen = set()
        for tri in triplets:
            for i in range(len(target)):
                if tri[i] > target[i]:
                    break
                elif tri[i] == target[i]:
                    seen.add(i)

        return len(seen) == len(target)
