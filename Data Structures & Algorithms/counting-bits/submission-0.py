class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for num in range(n+1):
            res.append(self.num_bit(num))
        return res
        
    def num_bit(self, num):
        res = 0
        while num:
            num = num & (num - 1)
            res += 1
        return res