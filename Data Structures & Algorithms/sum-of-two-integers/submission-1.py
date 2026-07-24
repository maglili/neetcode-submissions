class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        res = 0
        mask = 0xFFFFFFFF

        for i in range(32):
            bit_a = (a >> i) & 1
            bit_b = (b >> i) & 1
            cur_bit = bit_a ^ bit_b ^ carry
            carry = (bit_a & bit_b == 1) | (bit_a & carry == 1) | (bit_b & carry == 1)
            res = res | (cur_bit << i)

        if res > 0x7fffffff:
            res ^= mask
            res = ~(res)

        return res