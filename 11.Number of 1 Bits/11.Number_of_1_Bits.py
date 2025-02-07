class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n%2
            n=n>>1
        return res

#               (or)

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n>0:
            n = n&(n-1)
            res+=1
        return res



sol = Solution()
print(sol.hammingWeight(2147483645))