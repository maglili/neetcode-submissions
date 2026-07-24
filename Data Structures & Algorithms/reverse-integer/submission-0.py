class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        
        max_sign = 2147483647
        min_sign = -2147483648

        sign = 1 if x >= 0 else -1
        x = abs(x)

        while x:
            digit = x % 10
            x = x // 10
            
            if res >= max_sign:
                return 0

            res = (res * 10) + digit

        res = sign * res
        if res > max_sign or res < min_sign:
            return 0
        return res
