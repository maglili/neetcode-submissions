class Solution:
    def myPow(self, x: float, n: int) -> float:
        # base case
        if x == 0:
            return 0
        if n == 0:
            return 1

        res = self.myPow(x, abs(n) // 2)
        res = res * res

        if n % 2 != 0:
            res *= x

        return res if n >= 0 else 1 / res
