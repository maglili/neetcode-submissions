class Solution:
    def countBits(self, n: int) -> List[int]:
        # A[i] = A[ i & (i-1)] + bit0(num)
        A = [0] * (n + 1)
        for i in range(1, n+1):
            A[i] = A[i & (i-1)] + 1
        return A
