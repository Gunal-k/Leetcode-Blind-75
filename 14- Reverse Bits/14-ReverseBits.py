class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))
        return res

# Alternatively, you can use the commented-out method:
class Solution:
    def reverseBits(self, n: int) -> int:
        n = bin(n)[2:].zfill(32)
        n = n[::-1]
        return int(n, 2)

sol = Solution()
n = 0b00000010100101000001111010011100
print(sol.reverseBits(n))
