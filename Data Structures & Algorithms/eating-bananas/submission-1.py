class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        max_val = max(piles)

        l = 1
        r = max_val
        k = r
        while (l <= r):
            temp_k = math.floor(l + (r - l) / 2)

            # time
            time = 0
            for num in piles:
                time+= math.ceil(num / temp_k)
            
            if time > h:
                l = temp_k + 1
            else:
                k = temp_k
                r = temp_k - 1
        return k


