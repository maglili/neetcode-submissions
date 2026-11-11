class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            n = self.sum_of_sqr(n)
            print(n)
            if n == 1:
                return True

        return False

    def sum_of_sqr(self, n: int) -> int:
        res = 0
        while n:
            res += (n % 10) ** 2
            n //= 10
        return res
