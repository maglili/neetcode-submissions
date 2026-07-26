class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        res = 0
        for i in range(32):
            bit_a = (a >> i) & 1
            bit_b = (b >> i) & 1
            
            bit = bit_a ^ bit_b ^ carry
            carry = (bit_a & bit_b == 1) or (bit_a & carry == 1) or (bit_b & carry == 1)

            res = res | (bit << i)

        if res > 0x7fffffff:
            res -= 0x10000000

        return res