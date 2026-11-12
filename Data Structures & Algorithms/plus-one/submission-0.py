class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits) - 1
        src = 0
        for num in digits:
            src += num * (10**n)
            n -= 1

        src += 1

        res = []
        while src:
            res.append(src % 10)
            src //= 10

        return res[::-1]
