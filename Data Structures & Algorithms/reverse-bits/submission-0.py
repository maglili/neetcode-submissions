class Solution:
    def reverseBits(self, n: int) -> int:
        ori_binary = '{0:032b}'.format(n)
        new_binary = ori_binary[::-1]
        return int(new_binary, 2)