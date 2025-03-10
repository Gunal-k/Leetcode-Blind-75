class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.countPali(s, i, i)
            res += self.countPali(s, i, i + 1)
        return res
             
    def countPali(self, s, l, r):
        res = 0
        while r < len(s) and l >= 0 and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res

sol = Solution()
print(sol.countSubstrings('aab'))
